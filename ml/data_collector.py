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


cap=cv2.VideoCapture(0)

if not cap.isOpened:
    print("Error : Unable to open camera")
    exit()

while True:
    sucess,frame = cap.read()

    if not sucess:
        print("Error: Frame not read")
        break
    cv2.imshow("AI-Powered Virtual Yoga Trainer - Collect Dataset for Training", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()

# if __name__ == "__main__":