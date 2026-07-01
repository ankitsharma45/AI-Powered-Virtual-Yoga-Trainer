"""
===========================================================
                AI-Powered Virtual Yoga Trainer
===========================================================

Author      : Ankit Sharma
Institute   : Ajay Kumar Garg Engineering College
Course      : B.Tech (CSE - AI & ML)
Project     : AI Powered Virtual Yoga Trainer

File Name   : main.py

Description :
This is the main entry point of the project.
It is responsible for initializing and connecting
all project modules such as camera, pose detection,
pose classification, angle calculation, database,
and user interface.

Technologies:
- Python
- OpenCV
- MediaPipe
- NumPy

Version     : 1.0
Created On  : 2026
===========================================================
"""

# ---------------------------------------------------------
# Import detector module
# Ye pura AI Pose Detection system start karega
# ---------------------------------------------------------

from pose_detection.detector import run_detector


# ---------------------------------------------------------
# Program execution yahin se start hota hai
# __name__ check karta hai ki file directly run hui hai
# Agar kisi dusri file se import hui hai to ye block execute nahi hoga
# ---------------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print(" AI Powered Virtual Yoga Trainer Started ")
    print("=" * 60)

    # Detector module run karo
    run_detector()

    print("=" * 60)
    print(" Program Closed Successfully ")
    print("=" * 60)
