"""
===========================================================
                AI-Powered Virtual Yoga Trainer
===========================================================

Author      : Ankit Sharma
Institute   : Ajay Kumar Garg Engineering College
Course      : B.Tech (CSE - AI & ML)
Project     : AI Powered Virtual Yoga Trainer

File Name   : landmarks.py

Description :
This module contains the MediaPipe Pose landmark IDs.
Using named constants instead of numbers improves
code readability and maintainability.

Version     : 1.0
Created On  : 2026
===========================================================
"""

# -----------------------------
# Face
# -----------------------------
NOSE = 0

# -----------------------------
# Upper Body
# -----------------------------
LEFT_SHOULDER = 11
RIGHT_SHOULDER = 12

LEFT_ELBOW = 13
RIGHT_ELBOW = 14

LEFT_WRIST = 15
RIGHT_WRIST = 16

# -----------------------------
# Lower Body
# -----------------------------
LEFT_HIP = 23
RIGHT_HIP = 24

LEFT_KNEE = 25
RIGHT_KNEE = 26

LEFT_ANKLE = 27
RIGHT_ANKLE = 28


LANDMARK_NAMES = {
    NOSE: "Nose",

    LEFT_SHOULDER: "Left Shoulder",
    RIGHT_SHOULDER: "Right Shoulder",

    LEFT_ELBOW: "Left Elbow",
    RIGHT_ELBOW: "Right Elbow",

    LEFT_WRIST: "Left Wrist",
    RIGHT_WRIST: "Right Wrist",

    LEFT_HIP: "Left Hip",
    RIGHT_HIP: "Right Hip",

    LEFT_KNEE: "Left Knee",
    RIGHT_KNEE: "Right Knee",

    LEFT_ANKLE: "Left Ankle",
    RIGHT_ANKLE: "Right Ankle"
}