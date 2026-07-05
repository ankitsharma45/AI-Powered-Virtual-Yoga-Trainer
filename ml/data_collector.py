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
import csv
import os
import time

def save_to_csv(features, pose_name):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:

            header = []

            for i in range(33):
                header.extend([
                    f"x{i}",
                    f"y{i}",
                    f"z{i}",
                    f"v{i}"
                ])

            header.append("pose")

            writer.writerow(header)

        writer.writerow(features + [pose_name])

CSV_FILE = "dataset/yoga_pose_dataset.csv"
os.makedirs("dataset", exist_ok = True)

SAVE_DELAY = 1.0
last_save_time = 0

while True:
    pose_name = input("Enter Pose Name: ").strip().lower()

    if pose_name:
        break

    print("Pose name cannot be empty.")


# MediaPipe Pose Shortcut
mp_pose = mp.solutions.pose

with mp_pose.Pose(
    static_image_mode=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as pose:

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
                features = []
                if results.pose_landmarks:
        
                        mp_draw.draw_landmarks(
                                frame,
                                results.pose_landmarks,
                                mp_pose.POSE_CONNECTIONS
                        )
                        for landmark in results.pose_landmarks.landmark:
                                features.extend([landmark.x, landmark.y, landmark.z, landmark.visibility])
                                # print(len(feature))
        



                cv2.imshow("AI-Powered Virtual Yoga Trainer - Dataset Collector", frame)

                key = cv2.waitKey(1) & 0xFF

                
                if key == ord("s"):
                        current_time=time.time()
                        if len(features) == 132:
                                if current_time - last_save_time >= SAVE_DELAY:
                                        save_to_csv(features, pose_name)
                                        print(f"{pose_name.capitalize()} Pose Saved Successfully.")
                                        last_save_time = current_time
                                else:
                                       print("Please wait 1 sec before saving another sample.")
                        else:
                                print("No Pose Detected")
                if key == ord("q"):
                        break


    
cap.release()
cv2.destroyAllWindows()
