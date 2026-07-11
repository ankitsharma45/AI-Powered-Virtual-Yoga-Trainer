# AI-Powered Virtual Yoga Trainer

An AI-powered real-time yoga pose detection and classification system built using Computer Vision and Machine Learning.

## Project Overview

The AI-Powered Virtual Yoga Trainer detects human body landmarks using MediaPipe Pose and classifies yoga poses using a Machine Learning model.

The system processes real-time camera frames, extracts body landmark features, and predicts the yoga pose performed by the user.

## Current Project Status

- Camera Integration
- Real-Time Pose Detection
- MediaPipe Pose Landmark Extraction
- 33 Body Landmark Detection
- 132 Landmark Feature Extraction
- CSV Dataset Collector
- Pose-wise Sample Counter
- Dataset Collection
- Train-Test Split
- Random Forest Model Training
- Model Evaluation
- Model Accuracy: 98.69%
- Classification Report
- Confusion Matrix
- Trained Model Saving
- Real-Time Pose Prediction

## Currently Supported Poses

- T Pose
- Tree Pose
- Chair Pose

## Dataset

The dataset is created using MediaPipe Pose landmarks.

Each sample contains:

- 33 body landmarks
- X coordinate
- Y coordinate
- Z coordinate
- Visibility score

Total features:

33 landmarks × 4 values = 132 features

The target column contains the yoga pose name.

## Machine Learning Model

The current system uses a Random Forest Classifier for yoga pose classification.

Current test accuracy:

98.69%

## Technologies Used

- Python
- OpenCV
- MediaPipe
- Pandas
- Scikit-learn
- Random Forest
- Pickle
- Git
- GitHub

## Project Structure

AI_Yoga_Trainer/
- dataset/
  - yoga_pose_dataset.csv
- ml/
  - data_collector.py
  - train_model.py
  - predictor.py
- models/
  - yoga_pose_model.pkl
- pose_classification (for Rule based pose Detection)
  - classifier.py
  - pose_rules.py
- pose_detection
  - angles.py
  - detector.py
  - landmarks.py
  - utils.py
- README.md

## Current Development Issue

The current classifier always predicts one of the known yoga pose classes.

For example, a normal standing posture may be classified as a T Pose.

The next development phase will focus on:

- Unknown pose detection
- Confidence threshold
- Prediction stability
- Real-time prediction UI
- Yoga pose correction

## Author

Ankit Sharma