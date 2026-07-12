# AI-Powered Virtual Yoga Trainer

An AI-powered real-time yoga pose detection, classification, and correction system built using Computer Vision and Machine Learning.

## Project Overview

The AI-Powered Virtual Yoga Trainer is a real-time computer vision system designed to recognize yoga poses and provide a foundation for posture correction.

The system uses MediaPipe Pose to detect human body landmarks from live camera frames. A Machine Learning model analyzes the extracted landmark features and predicts the yoga pose performed by the user.

The project also contains a rule-based pose analysis module for joint angle calculation and pose correction logic.

## Current Project Status

- Camera Integration
- Real-Time Pose Detection
- MediaPipe Pose Landmark Extraction
- 33 Body Landmark Detection
- 132 Landmark Feature Extraction
- CSV Dataset Collector
- Pose-wise Sample Counter
- Custom Yoga Pose Dataset Collection
- Train-Test Dataset Split
- Random Forest Model Training
- Model Evaluation
- Classification Report
- Confusion Matrix
- Trained Model Persistence
- Real-Time Pose Prediction
- Unknown Pose Dataset Support
- Rule-Based Pose Analysis
- Joint Angle Calculation

### In Development

- Confidence-Based Pose Rejection
- Stable Prediction and Prediction Smoothing
- Real-Time Prediction UI
- Pose Validation
- Joint-Based Corrective Feedback
- Yoga Pose Correction System

## Currently Supported Pose Classes

- T Pose
- Tree Pose
- Chair Pose
- Goddess Pose
- Unknown / Non-Target Posture

The `unknown` class contains non-target and natural body postures to help reduce false classification of normal standing positions as yoga poses.

## Dataset

The dataset is custom collected using the project's real-time dataset collector and MediaPipe Pose.

Each captured sample represents one detected human pose.

For every sample, MediaPipe provides 33 body landmarks.

Each landmark contains:

- X coordinate
- Y coordinate
- Z coordinate
- Visibility score

Therefore:

33 landmarks × 4 values = 132 input features

The dataset also contains one target column named `pose`, which represents the pose class.

Dataset structure:

132 landmark features + 1 target label

The generated CSV dataset is stored locally and ignored by Git to avoid tracking continuously changing training data.

## Machine Learning Pipeline

The Machine Learning pipeline follows these steps:

1. Collect real-time pose landmarks using MediaPipe.
2. Save 132 landmark features into the CSV dataset.
3. Load and inspect the dataset using Pandas.
4. Separate input features (`X`) and target labels (`y`).
5. Split the dataset into training and testing sets.
6. Preserve class distribution using stratified splitting.
7. Train a Random Forest Classifier.
8. Predict pose classes on unseen test samples.
9. Evaluate the model using accuracy, precision, recall, and F1-score.
10. Analyze classification errors using a confusion matrix.
11. Save the trained model as a Pickle file.
12. Load the saved model for real-time pose prediction.

## Machine Learning Model

The current pose classification system uses a Random Forest Classifier.

Random Forest was selected as the initial Machine Learning model because the project uses structured numerical landmark features rather than raw image pixels.

The model receives 132 pose landmark features and predicts the corresponding pose class.

The trained model is saved as:

`models/yoga_pose_model.pkl`

## Real-Time Prediction Pipeline

Camera Frame
↓
MediaPipe Pose Detection
↓
33 Body Landmarks
↓
132 Landmark Features
↓
Random Forest Classifier
↓
Pose Prediction

The real-time predictor currently classifies detected body landmarks into one of the trained pose classes.

Confidence-based rejection and prediction smoothing are planned to improve prediction stability.

## Pose Correction Architecture

Pose classification and pose correction are treated as separate tasks.

Machine Learning Model:
Identifies which yoga pose the user is attempting.

Rule-Based Pose Analysis:
Analyzes joint angles and pose-specific rules to evaluate posture correctness.

Planned correction pipeline:

Pose Prediction
↓
Pose-Specific Rules
↓
Joint Angle Analysis
↓
Pose Validation
↓
Corrective Feedback

Example corrective feedback may include:

- Straighten your left arm.
- Bend your knee further.
- Raise your arm.
- Adjust your hip position.

## Technologies Used

- Python
- OpenCV
- MediaPipe
- Pandas
- Scikit-learn
- Random Forest Classifier
- Pickle
- Git
- GitHub

## Project Structure

AI_Yoga_Trainer/
├── dataset/
│   └── yoga_pose_dataset.csv
│
├── ml/
│   ├── data_collector.py
│   ├── train_model.py
│   └── predictor.py
│
├── models/
│   └── yoga_pose_model.pkl
│
├── pose_classification/
│   ├── classifier.py
│   └── pose_rules.py
│
├── pose_detection/
│   ├── angles.py
│   ├── detector.py
│   ├── landmarks.py
│   └── utils.py
│
├── .gitignore
└── README.md

## Current Development Focus

The current development phase focuses on improving real-time pose prediction.

Current challenges include:

- Normal postures may occasionally be classified as a known yoga pose.
- An imperfect yoga pose may still be recognized as the closest pose class.
- Frame-by-frame predictions may require stability improvements.

The next development phase will implement:

- Prediction confidence scores
- Confidence threshold
- Unknown pose rejection
- Prediction smoothing
- Pose-specific validation
- Joint angle-based correction
- Real-time corrective feedback

## Future Scope

- Support for additional yoga poses
- Real-time pose correction
- Voice-based corrective feedback
- User practice session tracking
- Pose accuracy scoring
- Progress monitoring
- Web-based user interface
- User authentication and session history

## Author

Ankit Sharma