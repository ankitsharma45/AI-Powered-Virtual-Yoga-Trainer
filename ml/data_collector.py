"""
===========================================================
        AI Powered Virtual Yoga Trainer
===========================================================

Module : Dataset Collector

Author : Ankit Sharma

Description:
This module collects pose landmarks from MediaPipe
and prepares the dataset for Machine Learning.

Current Goal:
✔ Camera
✔ Pose Detection
❌ CSV Saving (Later)
❌ Model Training (Later)

===========================================================
"""

import cv2
import mediapipe as mp


# MediaPipe Pose Shortcut
mp_pose = mp.solutions.pose

# Drawing Utility
mp_draw = mp.solutions.drawing_utils