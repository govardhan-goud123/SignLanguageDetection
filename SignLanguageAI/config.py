from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

DATASET_DIR = PROJECT_ROOT / "Indian"
MODEL_DIR = PROJECT_ROOT / "model"
MODEL_PATH = MODEL_DIR / "sign_language_model.joblib"
LABELS_PATH = MODEL_DIR / "labels.json"
CACHE_PATH = MODEL_DIR / "landmark_cache.npz"
REPORT_PATH = MODEL_DIR / "training_report.json"

CAMERA_INDEX = 0
CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720

MIRROR_CAMERA = True

MIN_DETECTION_CONFIDENCE = 0.50
MIN_TRACKING_CONFIDENCE = 0.50

# Only classes that actually exist in the Indian folder are used.
# Typical classes are A-Z. If 0-9 folders exist, they will also be trained.
SUPPORTED_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".bmp", ".webp"
}
