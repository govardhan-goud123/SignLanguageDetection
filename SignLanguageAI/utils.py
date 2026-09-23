from pathlib import Path
import json
import cv2
import numpy as np


def ensure_model_dir(model_dir: Path):
    model_dir.mkdir(parents=True, exist_ok=True)


def find_class_images(dataset_dir: Path, supported_extensions):
    """
    Finds images recursively.

    The class is assumed to be the name of the folder containing the image.
    Example:
        Indian/A/001.jpg -> class A
        Indian/B/hello.png -> class B
    """
    samples = []

    if not dataset_dir.exists():
        return samples

    for path in dataset_dir.rglob("*"):
        if not path.is_file():
            continue

        if path.suffix.lower() not in supported_extensions:
            continue

        # Folder immediately containing the image is treated as the label.
        label = path.parent.name.strip()

        if not label:
            continue

        samples.append((path, label))

    return samples


def load_image(path: Path):
    image = cv2.imread(str(path))
    if image is None:
        return None

    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def normalize_landmarks(landmarks):
    """
    Convert 21 x 3 landmarks into a translation/scale normalized
    63-value feature vector.

    Wrist becomes the origin.
    The largest absolute coordinate becomes the scale.
    """
    points = np.array(
        [[lm.x, lm.y, lm.z] for lm in landmarks],
        dtype=np.float32
    )

    # Make wrist the origin.
    points = points - points[0]

    # Scale normalization.
    scale = np.max(np.linalg.norm(points[:, :2], axis=1))

    if scale < 1e-6:
        return None

    points = points / scale

    return points.flatten()


def save_json(path: Path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
