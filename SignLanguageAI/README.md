# Indian Sign Language AI - PyCharm Project

This project recognizes **static Indian Sign Language hand signs** from a webcam using:

* OpenCV - webcam and display
* MediaPipe Hands - detects 21 hand landmarks
* Scikit-learn Random Forest - sign classification
* Joblib - saves the trained AI model

## Project Structure

```text
SignLanguageAI/
│
├── .venv/
├── Indian/
│   ├── A/
│   ├── B/
│   ├── C/
│   ├── ...
│   └── Z/
│
├── model/
├── main.py
├── train.py
├── config.py
├── utils.py
├── test_mediapipe.py
├── requirements.txt
├── run_app.bat
├── run_train.bat
└── README.md
```

## 1. Virtual Environment

This project uses the `.venv` virtual environment inside the `SignLanguageAI` folder.

Open Command Prompt and go to the project:

```bat
cd "C:\Users\Govardhan Goud\Downloads\SignLanguageAI_PyCharm_MediaPipe\SignLanguageAI"
```

Activate the environment:

```bat
.venv\Scripts\activate
```

The terminal should then show:

```text
(.venv) C:\Users\Govardhan Goud\Downloads\SignLanguageAI_PyCharm_MediaPipe\SignLanguageAI>
```

Always activate `.venv` before running the project.

## 2. Python Version

Use the Python version configured inside the existing `.venv`.

Check it with:

```bat
python --version
```

Do not use the global Python installation when running this project.

## 3. Install Dependencies

After activating `.venv`:

```bat
python -m pip install -r requirements.txt
```

Check MediaPipe:

```bat
python -c "import mediapipe as mp; print(mp.__version__)"
```

## 4. Dataset

Place the Indian Sign Language dataset inside:

```text
SignLanguageAI/
└── Indian/
    ├── A/
    ├── B/
    ├── C/
    ├── ...
    └── Z/
```

Each folder contains images for that particular sign.

Example:

```text
Indian/
├── A/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── B/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── Z/
    ├── image1.jpg
    └── ...
```

## 5. Test MediaPipe

Before training, test the webcam and MediaPipe:

```bat
python test_mediapipe.py
```

The program should detect the hand and display the **21 hand landmarks**.

Press:

```text
Q
```

to close the webcam.

## 6. Train the AI Model

Make sure the `Indian` dataset is available.

Run:

```bat
python train.py
```

The training process is:

```text
Dataset Images
      ↓
MediaPipe Hands
      ↓
21 Hand Landmarks
      ↓
Feature Extraction
      ↓
Normalization
      ↓
Random Forest
      ↓
Trained AI Model
```

After training, the model files are saved in:

```text
model/
├── sign_language_model.joblib
├── labels.json
├── training_report.json
└── landmark_cache.npz
```

## 7. Start the Webcam AI

After training:

```bat
python main.py
```

The application opens the webcam and predicts the sign in real time.

It displays:

* Hand bounding box
* 21 hand landmarks
* Predicted sign
* Confidence
* FPS

Example:

```text
Prediction: A
Confidence: 94%
```

## 8. Controls

```text
Q = Quit
R = Reload Model
```

## 9. How the AI Works

```text
Indian Sign Language Images
             ↓
          OpenCV
             ↓
      MediaPipe Hands
             ↓
      21 Hand Landmarks
             ↓
    Landmark Normalization
             ↓
       Random Forest
             ↓
       Sign Prediction
             ↓
        A / B / C / ... / Z
```

MediaPipe first detects the hand and extracts 21 important points.

These points are converted into numerical features.

The Random Forest model then uses those features to predict the sign.

## 10. Static Sign Recognition

This project currently recognizes **static hand signs**.

For example:

```text
Show A → A
Show B → B
Show C → C
Show D → D
...
Show Z → Z
```

This version does not understand complete sentences or continuous natural-language sign sequences.

For example:

```text
HELLO
HOW ARE YOU
GOOD MORNING
```

would require temporal sequence processing and a word/phrase dataset.

## 11. Webcam Mirror

The webcam can behave like a selfie camera.

Open:

```text
config.py
```

For mirrored webcam:

```python
MIRROR_CAMERA = True
```

For normal camera orientation:

```python
MIRROR_CAMERA = False
```

## 12. Camera Problems

The default camera is:

```python
CAMERA_INDEX = 0
```

If the webcam does not open, try:

```python
CAMERA_INDEX = 1
```

inside `config.py`.

## 13. Low Prediction Confidence

If the prediction is incorrect or confidence is low:

* Use good lighting.
* Show one hand clearly.
* Keep the complete hand inside the camera.
* Keep fingers visible.
* Avoid covering the hand.
* Keep the hand reasonably close to the camera.
* Try to match the orientation used in the dataset.

## 14. Wrong Predictions

The model learns from the training dataset.

If your webcam hand looks different from the training images, the model may predict another sign.

More varied training images can improve the model:

* Different hand sizes
* Different lighting
* Different backgrounds
* Different rotations
* Different camera distances
* More examples per class

## 15. Training Cache

During training, MediaPipe landmark features can be stored in:

```text
model/landmark_cache.npz
```

This can make later training faster when the dataset has not changed.

## 16. Complete Workflow

### Step 1 - Open Command Prompt

Go to the project:

```bat
cd "C:\Users\Govardhan Goud\Downloads\SignLanguageAI_PyCharm_MediaPipe\SignLanguageAI"
```

### Step 2 - Activate `.venv`

```bat
.venv\Scripts\activate
```

### Step 3 - Check Python

```bat
python --version
```

### Step 4 - Check MediaPipe

```bat
python -c "import mediapipe as mp; print(mp.__version__)"
```

### Step 5 - Test the Webcam

```bat
python test_mediapipe.py
```

### Step 6 - Train the Model

```bat
python train.py
```

### Step 7 - Start the AI

```bat
python main.py
```

## 17. Important

Always make sure the terminal starts with:

```text
(.venv)
```

before running:

```bat
python train.py
```

or:

```bat
python main.py
```

This ensures that the project uses the packages installed inside the project's virtual environment.

## Future Improvements

Possible future improvements include:

* Real-time word recognition
* Sentence recognition
* Multiple-hand detection
* Voice output
* Text-to-speech
* More Indian Sign Language words
* Temporal sequence recognition
* Deep learning models
* Better confidence filtering
* Web-based interface
* Real-time gesture-to-speech conversion

## Demo
![Sign Language Detection Demo](Screenshot (83).png))
