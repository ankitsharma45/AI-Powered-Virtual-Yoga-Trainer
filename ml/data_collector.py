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
✔ CSV Saving
❌ Model Training (Later)

===========================================================
"""

import cv2
import mediapipe as mp
import csv
import os
import time

# ab ham ek new csv create karke data enter karne ja rhe hai hai
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
# ab mai ek fn bnakar csv ke ander har pose ki row count karunga professional look ke liye
def get_sample_count(pose_name):
       if not os.path.isfile(CSV_FILE):
                return 0

       with open(CSV_FILE, "r" ) as file:
        reader = csv.reader(file)
        next(reader, None)
        count = 0
        for row in reader:
              if row[-1] == pose_name:
                    count+=1
       return count

CSV_FILE = "dataset/yoga_pose_dataset.csv"
os.makedirs("dataset", exist_ok = True)

SAVE_DELAY = 1.0
last_save_time = 0


#user se pose name lene ke liye 
while True:
    pose_name = input("Enter Pose Name: ").strip().lower()

    if pose_name:
        break

    print("Pose name cannot be empty.")

sample_count = get_sample_count(pose_name)
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
        
                cv2.rectangle(
                        frame,
                        (10,10),
                        (340,190),
                        (30,30,30),
                         -1 )
                cv2.putText(
                      frame,
                      f"Pose : {pose_name.capitalize()}",
                      (20, 40),
                      cv2.FONT_HERSHEY_SIMPLEX,
                      0.8,
                      (0, 255, 0),
                      2 )
                cv2.putText(
                        frame,
                        f"Samples : {sample_count}",
                        (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (255, 255, 0),
                        2 )

                cv2.putText(
                        frame,
                        "Press S : Save",
                        (20, 120),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 255),
                        2 )

                cv2.putText(
                        frame,
                        "Press Q : Quit",
                        (20, 160),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 255),
                        2 )
                cv2.imshow("AI-Powered Virtual Yoga Trainer - Dataset Collector", frame)
                key = cv2.waitKey(1) & 0xFF

                
                if key == ord("s"):
                        current_time=time.time()
                        if len(features) == 132:
                                if current_time - last_save_time >= SAVE_DELAY:
                                        save_to_csv(features, pose_name)
                                        print("Saved Successfully.")
                                        last_save_time = current_time
                                        sample_count += 1
                                else:
                                       print("Please wait 1 sec before saving another sample.")
                        else:
                                print("Status: No Pose Detected")
                if key == ord("q"):
                        break


    
cap.release()
cv2.destroyAllWindows()
