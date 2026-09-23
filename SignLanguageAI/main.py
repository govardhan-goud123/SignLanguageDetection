from pathlib import Path
import time

import cv2
import joblib
import mediapipe as mp
import numpy as np

from config import (
    MODEL_PATH,
    LABELS_PATH,
    CAMERA_INDEX,
    CAMERA_WIDTH,
    CAMERA_HEIGHT,
    MIRROR_CAMERA,
    MIN_DETECTION_CONFIDENCE,
    MIN_TRACKING_CONFIDENCE,
)
from utils import normalize_landmarks, load_json


def load_model():
    if not MODEL_PATH.exists():
        print("\nModel not found.")
        print("Run this first:")
        print("    python train.py")
        return None, None

    model = joblib.load(MODEL_PATH)

    labels = None
    if LABELS_PATH.exists():
        labels = load_json(LABELS_PATH).get("classes", [])

    return model, labels


def draw_hand(frame, hand_landmarks):
    """Draw MediaPipe landmarks and connections manually."""
    h, w = frame.shape[:2]

    # Same basic connections used by MediaPipe Hands.
    connections = [
        (0, 1), (1, 2), (2, 3), (3, 4),
        (0, 5), (5, 6), (6, 7), (7, 8),
        (5, 9), (9, 10), (10, 11), (11, 12),
        (9, 13), (13, 14), (14, 15), (15, 16),
        (13, 17), (17, 18), (18, 19), (19, 20),
        (0, 17)
    ]

    points = []

    for lm in hand_landmarks.landmark:
        x = int(lm.x * w)
        y = int(lm.y * h)
        points.append((x, y))

    # Draw connections.
    for a, b in connections:
        cv2.line(
            frame,
            points[a],
            points[b],
            (255, 180, 0),
            2,
            cv2.LINE_AA,
        )

    # Draw landmarks.
    for x, y in points:
        cv2.circle(
            frame,
            (x, y),
            5,
            (0, 0, 255),
            -1,
            cv2.LINE_AA,
        )

    # Bounding box.
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    x1 = max(min(xs) - 25, 0)
    y1 = max(min(ys) - 25, 0)
    x2 = min(max(xs) + 25, w - 1)
    y2 = min(max(ys) + 25, h - 1)

    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        (0, 140, 255),
        2,
    )

    return x1, y1, x2, y2


def draw_ui(frame, prediction, confidence, fps):
    h, w = frame.shape[:2]

    # Top information panel.
    cv2.rectangle(
        frame,
        (0, 0),
        (w, 95),
        (20, 20, 20),
        -1,
    )

    cv2.putText(
        frame,
        "INDIAN SIGN LANGUAGE",
        (25, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )

    if prediction:
        text = f"Prediction: {prediction}"
        conf_text = f"Confidence: {confidence * 100:.1f}%"
    else:
        text = "Show one hand"
        conf_text = "Confidence: --"

    cv2.putText(
        frame,
        text,
        (25, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 100),
        2,
        cv2.LINE_AA,
    )

    cv2.putText(
        frame,
        conf_text,
        (w - 280, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )

    cv2.putText(
        frame,
        f"FPS: {fps:.0f}",
        (w - 150, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )

    cv2.putText(
        frame,
        "Q: Quit   R: Reload",
        (20, h - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        1,
        cv2.LINE_AA,
    )


def main():
    model, labels = load_model()

    if model is None:
        return

    print("Starting webcam...")
    print("Press Q to quit.")
    print("Press R to reload the model.")

    cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

    if not cap.isOpened():
        # Fallback for systems where CAP_DSHOW is unavailable.
        cap.release()
        cap = cv2.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        print("\nERROR: Could not open webcam.")
        print("Try CAMERA_INDEX = 1 in config.py")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)

    mp_hands = mp.solutions.hands

    previous_time = time.time()
    fps = 0.0

    # Smooth prediction so the displayed result does not jump every frame.
    prediction_history = []
    HISTORY_SIZE = 5

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        model_complexity=0,
        min_detection_confidence=MIN_DETECTION_CONFIDENCE,
        min_tracking_confidence=MIN_TRACKING_CONFIDENCE,
    ) as hands:

        while True:
            success, frame = cap.read()

            if not success:
                print("Could not read camera frame.")
                break

            if MIRROR_CAMERA:
                frame = cv2.flip(frame, 1)

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            prediction = None
            confidence = 0.0

            if result.multi_hand_landmarks:
                hand_landmarks = result.multi_hand_landmarks[0]

                draw_hand(frame, hand_landmarks)

                features = normalize_landmarks(
                    hand_landmarks.landmark
                )

                if features is not None:
                    features = features.reshape(1, -1)

                    prediction = model.predict(features)[0]

                    if hasattr(model, "predict_proba"):
                        probabilities = model.predict_proba(features)[0]
                        confidence = float(np.max(probabilities))

                    prediction_history.append(prediction)

                    if len(prediction_history) > HISTORY_SIZE:
                        prediction_history.pop(0)

                    # Majority vote over recent frames.
                    values, counts = np.unique(
                        prediction_history,
                        return_counts=True
                    )
                    prediction = values[np.argmax(counts)]

            else:
                prediction_history.clear()

            # FPS.
            current_time = time.time()
            delta = current_time - previous_time
            previous_time = current_time

            if delta > 0:
                fps = 0.9 * fps + 0.1 * (1.0 / delta)

            draw_ui(
                frame,
                prediction,
                confidence,
                fps,
            )

            cv2.imshow(
                "Indian Sign Language AI - MediaPipe",
                frame
            )

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

            if key == ord("r"):
                print("\nReloading model...")
                model, labels = load_model()

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
