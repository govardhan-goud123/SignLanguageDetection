"""
Train the Indian Sign Language classifier.

Pipeline:
    Dataset image
        -> MediaPipe Hands
        -> 21 landmarks
        -> normalized 63 features
        -> Random Forest
        -> saved model
"""
from pathlib import Path
import time
import json
import warnings

import cv2
import joblib
import mediapipe as mp
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

from config import (
    DATASET_DIR,
    MODEL_DIR,
    MODEL_PATH,
    LABELS_PATH,
    CACHE_PATH,
    REPORT_PATH,
    MIN_DETECTION_CONFIDENCE,
    MIN_TRACKING_CONFIDENCE,
    SUPPORTED_EXTENSIONS,
)
from utils import (
    ensure_model_dir,
    find_class_images,
    normalize_landmarks,
    save_json,
)

warnings.filterwarnings("ignore")


def extract_features(samples):
    """
    Extract MediaPipe hand landmarks from all images.

    The cache is saved so subsequent training runs can skip MediaPipe
    processing when the dataset has not changed.
    """

    if CACHE_PATH.exists():
        try:
            cached = np.load(CACHE_PATH, allow_pickle=True)

            X = cached["X"]
            y = cached["y"].astype(str)

            if len(X) == len(samples):
                print("\nUsing existing landmark cache.")
                return X, y

            print("\nDataset size changed. Rebuilding landmark cache...")

        except Exception:
            print("\nCould not read cache. Rebuilding it...")

    mp_hands = mp.solutions.hands

    X = []
    y = []

    total = len(samples)
    start = time.time()

    with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        model_complexity=0,
        min_detection_confidence=MIN_DETECTION_CONFIDENCE,
        min_tracking_confidence=MIN_TRACKING_CONFIDENCE,
    ) as hands:

        for index, (path, label) in enumerate(samples, start=1):
            image = cv2.imread(str(path))

            if image is None:
                continue

            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            if not result.multi_hand_landmarks:
                continue

            landmarks = result.multi_hand_landmarks[0].landmark
            features = normalize_landmarks(landmarks)

            if features is None:
                continue

            X.append(features)
            y.append(label)

            if index % 100 == 0 or index == total:
                elapsed = time.time() - start
                rate = index / elapsed if elapsed > 0 else 0
                print(
                    f"\rProcessing {index}/{total} | "
                    f"usable: {len(X)} | "
                    f"{rate:.1f} images/sec",
                    end=""
                )

    print()

    if not X:
        raise RuntimeError(
            "MediaPipe could not detect a hand in the dataset images."
        )

    X = np.asarray(X, dtype=np.float32)
    y = np.asarray(y)

    np.savez_compressed(CACHE_PATH, X=X, y=y)

    return X, y


def main():
    ensure_model_dir(MODEL_DIR)

    print("=" * 65)
    print("       INDIAN SIGN LANGUAGE AI - MODEL TRAINING")
    print("=" * 65)

    if not DATASET_DIR.exists():
        print(f"\nERROR: Dataset folder not found:")
        print(DATASET_DIR)
        print("\nCreate this structure:")
        print("SignLanguageAI/")
        print("    Indian/")
        print("        A/")
        print("        B/")
        print("        ...")
        print("        Z/")
        return

    samples = find_class_images(DATASET_DIR, SUPPORTED_EXTENSIONS)

    if not samples:
        print("\nERROR: No images found inside the Indian folder.")
        print("Check that your class folders contain JPG/PNG images.")
        return

    # Sort for deterministic processing.
    samples.sort(key=lambda item: (item[1].lower(), str(item[0]).lower()))

    labels_in_dataset = sorted(set(label for _, label in samples))

    print(f"\nDataset folder : {DATASET_DIR}")
    print(f"Images found   : {len(samples):,}")
    print(f"Classes found  : {len(labels_in_dataset)}")
    print(f"Classes        : {', '.join(labels_in_dataset)}")

    print("\nStep 1/3 - Extracting MediaPipe landmarks...")
    X, y = extract_features(samples)

    labels = sorted(set(y.tolist()))

    print(f"\nUsable samples : {len(X):,}")
    print(f"Features/image : {X.shape[1]}")
    print(f"Classes        : {len(labels)}")

    counts = {}
    for label in labels:
        counts[label] = int(np.sum(y == label))

    print("\nSamples per class:")
    for label in labels:
        print(f"  {label:>5}: {counts[label]:>6,}")

    # A stratified split keeps every class represented in train/test.
    print("\nStep 2/3 - Training Random Forest...")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=None,
        min_samples_split=2,
        random_state=42,
        n_jobs=-1,
        class_weight="balanced_subsample",
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print("\nStep 3/3 - Evaluation")
    print("-" * 65)
    print(f"Test accuracy: {accuracy * 100:.2f}%")
    print("-" * 65)

    print("\nClassification report:")
    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0,
        )
    )

    joblib.dump(model, MODEL_PATH)

    save_json(
        LABELS_PATH,
        {
            "classes": labels,
            "num_classes": len(labels),
            "feature_count": int(X.shape[1]),
        },
    )

    report = {
        "accuracy": float(accuracy),
        "samples": int(len(X)),
        "features": int(X.shape[1]),
        "classes": labels,
        "samples_per_class": counts,
    }

    save_json(REPORT_PATH, report)

    print("\nModel saved:")
    print(MODEL_PATH)

    print("\nLabels saved:")
    print(LABELS_PATH)

    print("\nTraining completed successfully.")
    print("\nNow run:")
    print("    python main.py")


if __name__ == "__main__":
    main()
