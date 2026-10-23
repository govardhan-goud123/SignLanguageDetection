<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=800&size=32&pause=1000&color=00F7FF&center=true&vCenter=true&width=850&height=70&lines=INDIAN+SIGN+LANGUAGE+AI;THE+FUTURE+OF+GESTURE+RECOGNITION;REAL-TIME+COMPUTER+VISION" alt="Animated project title"/>

### INTELLIGENCE THAT UNDERSTANDS HAND SIGNS

<img src="https://img.shields.io/badge/ARTIFICIAL-INTELLIGENCE-00F7FF?style=for-the-badge&labelColor=080B18"/>
<img src="https://img.shields.io/badge/COMPUTER-VISION-7B61FF?style=for-the-badge&labelColor=080B18"/>
<img src="https://img.shields.io/badge/MACHINE-LEARNING-00E5A8?style=for-the-badge&labelColor=080B18"/>

<br>

*Transforming static hand gestures into recognizable letters through real-time AI.*

</div>

---

## SYSTEM OVERVIEW

<table>
<tr>
<td align="center" width="50%">

### VISION ENGINE

Hand detection and tracking using MediaPipe.

**21 Hand Landmarks**

</td>
<td align="center" width="50%">

### INTELLIGENCE ENGINE

Hand sign classification using a trained Random Forest model.

**Machine Learning**

</td>
</tr>
<tr>
<td align="center" width="50%">

### LIVE RECOGNITION

Real-time letter predictions displayed on the webcam feed.

**Instant Feedback**

</td>
<td align="center" width="50%">

### MODEL STORAGE

Save and reload the trained classifier for future predictions.

**Joblib Serialization**

</td>
</tr>
</table>

---

## LIVE DEMONSTRATION

<div align="center">

![Indian Sign Language AI Demo](demo.png)

*Real-time hand detection and static sign recognition.*

</div>

---

## TECHNOLOGY STACK

<div align="center">

<img src="https://skillicons.dev/icons?i=python,opencv,sklearn,git,github&theme=dark" alt="Technology stack"/>

</div>

| Technology      | Application                         |
| --------------- | ----------------------------------- |
| Python          | Core programming                    |
| OpenCV          | Webcam capture and image processing |
| MediaPipe Hands | Detection of 21 hand landmarks      |
| Scikit-learn    | Random Forest classification        |
| NumPy           | Numerical feature processing        |
| Joblib          | Model saving and loading            |
| JSON            | Label and training report storage   |
| PyCharm         | Development environment             |

---

## PROJECT ARCHITECTURE

<table>
<tr>
<th>COMPONENT</th>
<th>DESCRIPTION</th>
</tr>
<tr>
<td><code>main.py</code></td>
<td>Runs real-time webcam recognition.</td>
</tr>
<tr>
<td><code>train.py</code></td>
<td>Extracts features and trains the classifier.</td>
</tr>
<tr>
<td><code>config.py</code></td>
<td>Controls webcam and application settings.</td>
</tr>
<tr>
<td><code>utils.py</code></td>
<td>Contains reusable helper functions.</td>
</tr>
<tr>
<td><code>test_mediapipe.py</code></td>
<td>Tests webcam access and hand landmark detection.</td>
</tr>
<tr>
<td><code>requirements.txt</code></td>
<td>Lists the required Python packages.</td>
</tr>
<tr>
<td><code>model/</code></td>
<td>Stores the trained model and supporting files.</td>
</tr>
<tr>
<td><code>Indian/</code></td>
<td>Contains the labelled sign image dataset.</td>
</tr>
</table>

### DIRECTORY STRUCTURE

```text
SignLanguageAI/
│
├── .venv/
├── Indian/
│   ├── A/
│   ├── B/
│   ├── C/
│   └── ... Z/
│
├── model/
│   ├── sign_language_model.joblib
│   ├── labels.json
│   ├── training_report.json
│   └── landmark_cache.npz
│
├── main.py
├── train.py
├── config.py
├── utils.py
├── test_mediapipe.py
├── requirements.txt
├── run_app.bat
├── run_train.bat
├── demo.png
└── README.md
```

---

## GETTING STARTED

<table>
<tr>
<td width="65">

**01 — INITIALIZE**

Open Command Prompt and navigate to your project folder.

</td>
<td width="35">

```bat
cd "C:\Users\Govardhan Goud\Downloads\SignLanguageAI_PyCharm_MediaPipe\SignLanguageAI"
```

</td>
</tr>
<tr>
<td>

**02 — ACTIVATE ENVIRONMENT**

Use the project's existing virtual environment.

</td>
<td>

```bat
.venv\Scripts\activate
```

</td>
</tr>
<tr>
<td>

**03 — INSTALL DEPENDENCIES**

Install the packages listed in the requirements file.

</td>
<td>

```bat
python -m pip install -r requirements.txt
```

</td>
</tr>
<tr>
<td>

**04 — VERIFY MEDIAPIPE**

Check that MediaPipe is installed correctly.

</td>
<td>

```bat
python -c "import mediapipe as mp; print(mp.__version__)"
```

</td>
</tr>
</table>

---

## LAUNCH THE AI

<table>
<tr>
<td align="center" width="33%">

### TEST

Check hand detection.

```bat
python test_mediapipe.py
```

</td>
<td align="center" width="33%">

### TRAIN

Train the classifier.

```bat
python train.py
```

</td>
<td align="center" width="33%">

### RUN

Start live recognition.

```bat
python main.py
```

</td>
</tr>
</table>

**Controls**

| Key | Action                   |
| --- | ------------------------ |
| `Q` | Exit the application     |
| `R` | Reload the trained model |

---

## CORE CAPABILITIES

<table>
<tr>
<td width="50%" valign="top">

### HAND DETECTION

* Real-time webcam processing
* Detection of 21 hand landmarks
* Hand bounding box
* Landmark visualization

</td>
<td width="50%" valign="top">

### AI CLASSIFICATION

* Numerical feature extraction
* Random Forest prediction
* Predicted letter display
* Confidence score
* FPS monitoring

</td>
</tr>
</table>

---

## MODEL CONFIGURATION

### Webcam Settings

Inside `config.py`:

```python
CAMERA_INDEX = 0
MIRROR_CAMERA = True
```

If the webcam does not open, try changing `CAMERA_INDEX` to `1`.

Set `MIRROR_CAMERA = False` if you prefer a normal, non-mirrored camera view.

### Training Outputs

| File                         | Purpose                                |
| ---------------------------- | -------------------------------------- |
| `sign_language_model.joblib` | Trained classifier                     |
| `labels.json`                | Class labels                           |
| `training_report.json`       | Training or evaluation information     |
| `landmark_cache.npz`         | Cached landmark features, if generated |

---

## CURRENT PROJECT STATUS

<table>
<tr>
<th>FEATURE</th>
<th>STATUS</th>
</tr>
<tr>
<td>Webcam integration</td>
<td>Implemented</td>
</tr>
<tr>
<td>Hand landmark detection</td>
<td>Implemented</td>
</tr>
<tr>
<td>Static sign classification</td>
<td>Core functionality</td>
</tr>
<tr>
<td>Live predictions</td>
<td>Implemented</td>
</tr>
<tr>
<td>Dynamic gesture recognition</td>
<td>Planned</td>
</tr>
<tr>
<td>Word and sentence recognition</td>
<td>Planned</td>
</tr>
<tr>
<td>Text-to-speech</td>
<td>Planned</td>
</tr>
<tr>
<td>Web application</td>
<td>Planned</td>
</tr>
</table>

The current version focuses on static hand poses representing supported letters. It does not yet translate continuous Indian Sign Language into complete sentences.

---

## FUTURE DEVELOPMENT

<table>
<tr>
<td width="50%" valign="top">

### DYNAMIC GESTURES

Use LSTMs, GRUs, or Transformers to analyze hand movements over time.

</td>
<td width="50%" valign="top">

### WORD RECOGNITION

Expand the dataset to include a verified vocabulary of Indian Sign Language words.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### VOICE OUTPUT

Convert recognized text into speech using a text-to-speech engine.

</td>
<td width="50%" valign="top">

### TWO-HAND DETECTION

Extend the system to recognize signs that require both hands.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### SMART PREDICTIONS

Apply confidence thresholds and temporal smoothing to improve prediction stability.

</td>
<td width="50%" valign="top">

### WEB INTERFACE

Develop an accessible browser-based interface for demonstrations.

</td>
</tr>
</table>

---

## TROUBLESHOOTING

<table>
<tr>
<td width="35%">

**Webcam not opening**

</td>
<td>

Check camera permissions, close other applications using the webcam, and verify `CAMERA_INDEX`.

</td>
</tr>
<tr>
<td>

**MediaPipe import error**

</td>
<td>

Activate `.venv` and install dependencies using `requirements.txt`.

</td>
</tr>
<tr>
<td>

**Incorrect predictions**

</td>
<td>

Check dataset labels, lighting, hand visibility, and training data variety.

</td>
</tr>
<tr>
<td>

**Model not found**

</td>
<td>

Run `python train.py` and verify that the model files exist.

</td>
</tr>
</table>

---

<div align="center">

## THE VISION

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=600&size=22&pause=1200&color=00F7FF&center=true&vCenter=true&width=750&height=50&lines=GESTURES+INTO+INTELLIGENCE;COMPUTER+VISION+MEETS+HUMAN+COMMUNICATION;BUILDING+ACCESSIBILITY+THROUGH+AI" alt="Animated closing text"/>

**INDIAN SIGN LANGUAGE AI**

*Exploring the intersection of computer vision, machine learning, and accessibility.*

<br>

<img src="https://img.shields.io/badge/BUILT%20WITH-PYTHON-00F7FF?style=for-the-badge&labelColor=080B18"/>
<img src="https://img.shields.io/badge/POWERED%20BY-AI-7B61FF?style=for-the-badge&labelColor=080B18"/>

</div>
