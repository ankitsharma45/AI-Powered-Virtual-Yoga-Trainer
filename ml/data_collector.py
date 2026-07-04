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

pose = mp_pose.Pose(
    static_image_mode=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Drawing Utility
mp_draw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open camera")
    exit()

while True:
    success, frame = cap.read()

    if not success:
        print("Error: Frame not read")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)

    if results.pose_landmarks:

        mp_draw.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
        )



    cv2.imshow("AI-Powered Virtual Yoga Trainer - Dataset Collector", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
