"""
===========================================================
                AI-Powered Virtual Yoga Trainer
===========================================================

Author      : Ankit Sharma
Institute   : Ajay Kumar Garg Engineering College
Course      : B.Tech (CSE - AI & ML)
Project     : AI Powered Virtual Yoga Trainer

File Name   : utils.py

Description :
This module contains reusable utility functions
used across the project.

Responsibilities:
• Draw landmarks
• Draw body joints
• Display labels
• Draw custom circles
• Display text
• Helper functions for visualization

Note:
This module is created to avoid code duplication
and improve project maintainability.

Technologies:
- OpenCV

Version     : 1.0
Created On  : 2026
===========================================================
"""

import cv2

# common funtion for all 33 points
def draw_label(frame, landmark, width, height):  
    x=int(landmark.x * width)
    y=int(landmark.y * height)

    # Safety check
    x = max(0, min(width - 1, x))
    y = max(0, min(height - 1, y))

    cv2.circle(frame,(x,y),8,(0,0,255),-1)
    # cv2.putText(frame,label,(nose_x, nose_y - 20),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0, 0, 255),2)    ----> for add text above the data point, make sure add onemore parameter called label in drawlabwel


