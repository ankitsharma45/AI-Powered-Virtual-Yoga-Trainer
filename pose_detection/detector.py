"""
===========================================================
                AI-Powered Virtual Yoga Trainer
===========================================================

Author      : Ankit Sharma
Institute   : Ajay Kumar Garg Engineering College
Course      : B.Tech (CSE - AI & ML)
Project     : AI Powered Virtual Yoga Trainer

File Name   : detector.py

Description :
This module performs real-time human pose detection
using the MediaPipe Pose solution.

Responsibilities:
• Capture live video from camera
• Detect 33 human body landmarks
• Draw body skeleton
• Return landmark coordinates
• Provide input for angle calculation
  and pose classification modules

Technologies:
- OpenCV
- MediaPipe
- NumPy

Version     : 1.0
Created On  : 2026
===========================================================
"""


# OpenCV library import kar rahe hain
# Iska use camera aur image processing ke liye hota hai
import cv2
from .utils import draw_label # this is for landmark extraction
from .landmarks import *
from pose_classification.classifier import classify_joint
from .angles import  get_joint_angle  # ye calculate hue angle ko lene ke liye
# import poses rule from pose_rule.py se
from pose_classification.pose_rules import *



# MediaPipe library import kar rahe hain
# Ye AI based pose detection ke liye use hogi
import mediapipe as mp

# MediaPipe ke Pose module ka shortcut bana rahe hain
# Iske through body landmarks detect karenge
mp_pose = mp.solutions.pose

# MediaPipe Drawing Utility
# Ye landmarks aur skeleton draw karne ke liye use hoti hai
mp_draw = mp.solutions.drawing_utils

def run_detector():
    # Camera start kar rahe hain
    # 0 ka matlab default camera
    # Baad mein yahan phone camera URL bhi use kar sakte hain
    # url = "http://[2402:8100:26d0:b5a6::e7]:8080/video"
    camera_source=0
    cap = cv2.VideoCapture(camera_source)

    # Pose model load kar rahe hain
    # with use karne se resources automatically release ho jate hain
    with mp_pose.Pose(

        # Minimum confidence for first pose detection
        # 0.5 = 50% confidence required
        min_detection_confidence=0.5,

        # Tracking confidence
        # Agar pose mil gaya hai to usko track karega
        min_tracking_confidence=0.5

    ) as pose:

        # Infinite loop
        # Camera continuously frames read karega
        while True:

            # Camera se ek frame read karo
            success, frame = cap.read()

            # Agar frame nahi mila
            # to loop break kar do
            if not success:
                print("Frame not received")
                break

            # OpenCV image ko BGR format me read karta hai
            # MediaPipe RGB format expect karta hai
            # Isliye conversion zaroori hai
            rgb_frame = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            # AI model ko frame bhej rahe hain
            # Ye body detect karega
            results = pose.process(rgb_frame)

            # Agar body detect ho gayi hai
            if results.pose_landmarks:

                # Body skeleton draw karo
                mp_draw.draw_landmarks(

                    # Kis image par draw karna hai
                    frame,

                    # Detected landmarks
                    results.pose_landmarks,

                    # Landmarks ke beech connections
                    mp_pose.POSE_CONNECTIONS,

                    # Landmark Dots Style
                    mp_draw.DrawingSpec(
                        color=(255,255,0),  # White Dots
                        thickness=3,
                        circle_radius=4
                    ),

                    # Connection Lines Style
                    mp_draw.DrawingSpec(
                        color=(255,0,0),
                        thickness=3,
                        circle_radius=2
                    )
                )

                # Frame ki height aur width nikal rahe hain
                height, width, _ = frame.shape

                point_list=([NOSE,LEFT_SHOULDER,RIGHT_SHOULDER,LEFT_ELBOW,RIGHT_ELBOW,LEFT_WRIST,RIGHT_WRIST,LEFT_HIP,RIGHT_HIP,LEFT_KNEE,RIGHT_KNEE,LEFT_ANKLE,RIGHT_ANKLE])
                for i in point_list:
                    draw_label(frame,results.pose_landmarks.landmark[i],width,height)

                

                # # Nose ke cordinate se usse explore kar rhe hai, ese hi one by one sabhi ko kar sakte hai aur ek function ke help se code ko optimise karenge
                # nose=results.pose_landmarks.landmark[0]
                # # print("nose:",nose)

                # # Nose ke normalized coordinates ko pixel me convert kar rahe hain
                # nose_x = int(nose.x * width)
                # nose_y = int(nose.y * height)

                # # Nose par ek red circle draw kar rahe hain
                # cv2.circle(frame,(nose_x, nose_y),8,(0, 0, 255),-1)

                # #ye line red circle ki jagah uske upar text likhne ke liye hai
                # # cv2.putText(frame,"NOSE",(nose_x, nose_y - 20),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0, 0, 255),2)

                # #--------Left Shopulder
                # l_shoulder=results.pose_landmarks.landmark[11]
                # # print("leftS:",l_shoulder)
                # l_shoulder_x=int(l_shoulder.x * width)
                # l_shoulder_y=int(l_shoulder.y * height)
                # cv2.circle(frame,(l_shoulder_x,l_shoulder_y),8,(0,0,255),-1)

                # #-------- Right Shoulder
                # r_shoulder=results.pose_landmarks.landmark[12]
                # # print("RightS:",r_shoulder)
                # r_shoulder_x=int(r_shoulder.x * width)
                # r_shoulder_y=int(r_shoulder.y * height)
                # cv2.circle(frame,(r_shoulder_x,r_shoulder_y),8,(0,0,255),-1)

                # left_shoulder=results.pose_landmarks.landmark[LEFT_SHOULDER]
                # left_wrist=results.pose_landmarks.landmark[LEFT_WRIST]
                # left_elbow=results.pose_landmarks.landmark[LEFT_ELBOW]
                # right_shoulder=results.pose_landmarks.landmark[RIGHT_SHOULDER]      # ye sab line cordinate ko lene ke liye hai -> x,y,z,visiblity
                # right_wrist=results.pose_landmarks.landmark[RIGHT_WRIST]             # lekin hame sirf x,y chahiye toh abham ishmese x,y alagkarenge
                # right_elbow=results.pose_landmarks.landmark[RIGHT_ELBOW]


                # for right shoulder
                right_shoulder_angle= get_joint_angle(results.pose_landmarks.landmark,RIGHT_ELBOW,RIGHT_SHOULDER,RIGHT_HIP)
                # right_shoulder_status = classify_joint(right_shoulder_angle)
                cv2.putText(frame, f"Right Shoulder : {right_shoulder_angle} deg",(30,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                # cv2.putText(frame,f"Right Shoulder Status : {right_shoulder_status}",(30,80),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)

               # for left shoulder
                left_shoulder_angle= get_joint_angle(results.pose_landmarks.landmark,LEFT_ELBOW,LEFT_SHOULDER,LEFT_HIP)
                # left_shoulder_status = classify_joint(left_shoulder_angle)
                cv2.putText(frame, f"Left Shoulder : {left_shoulder_angle} deg",(30,120),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                # cv2.putText(frame,f"Left Shoulder Status : {left_shoulder_status}",(30,160),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)

                # for right elbow
                right_elbow_angle= get_joint_angle(results.pose_landmarks.landmark,RIGHT_SHOULDER,RIGHT_ELBOW,RIGHT_WRIST)
                right_elbow_status = classify_joint(right_elbow_angle)
                cv2.putText(frame, f"Right Elbow : {right_elbow_angle} deg",(30,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                cv2.putText(frame,f"Right Elbow Status : {right_elbow_status}",(30,240),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)
            

                # for left elbow
                left_elbow_angle= get_joint_angle(results.pose_landmarks.landmark,LEFT_SHOULDER,LEFT_ELBOW,LEFT_WRIST)
                left_elbow_status = classify_joint(left_elbow_angle)
                cv2.putText(frame, f"Left Elbow : {left_elbow_angle} deg",(30,280),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                cv2.putText(frame,f"Left Elbow Status : {left_elbow_status}",(30,320),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)

               # for right hip
                right_hip_angle= get_joint_angle(results.pose_landmarks.landmark,RIGHT_SHOULDER,RIGHT_HIP,RIGHT_KNEE)
                # right_hip_status = classify_joint(right_hip_angle)
                cv2.putText(frame, f"Right Hip : {right_hip_angle} deg",(30,360),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                # cv2.putText(frame,f"Right Hip Status : {right_hip_status}",(30,400),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)

               # for left hip
                left_hip_angle= get_joint_angle(results.pose_landmarks.landmark,LEFT_SHOULDER,LEFT_HIP,LEFT_KNEE)
                # left_hip_status = classify_joint(left_hip_angle)
                cv2.putText(frame, f"Left Hip : {left_hip_angle} deg",(30,440),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                # cv2.putText(frame,f"Left Hip Status : {left_hip_status}",(30,480),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)

               # for right knee
                right_knee_angle= get_joint_angle(results.pose_landmarks.landmark,RIGHT_HIP,RIGHT_KNEE,RIGHT_ANKLE)
                # right_knee_status = classify_joint(right_knee_angle)
                cv2.putText(frame, f"Right Knee : {right_knee_angle} deg",(30,520),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                # cv2.putText(frame,f"Right Knee Status : {right_knee_status}",(30,560),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)

               # for left knee
                left_knee_angle= get_joint_angle(results.pose_landmarks.landmark,LEFT_HIP,LEFT_KNEE,LEFT_ANKLE)
                # left_knee_status = classify_joint(left_knee_angle)
                cv2.putText(frame, f"Left Knee : {left_knee_angle} deg",(30,600),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                # cv2.putText(frame,f"Left Knee Status : {left_knee_status}",(30,640),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)


                # funtion ko call kar rhe hai T pose ke liye
                # t_pose = detect_t_pose(left_elbow_angle,right_elbow_angle,left_shoulder_angle,right_shoulder_angle)
                # if t_pose:
                #     cv2.putText(frame,"Pose : T Pose",(width - 280, 40),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0),2)

                # else:
                #     cv2.putText(frame,"Pose : Unknown",(width - 280, 40),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255),2)

                # #Tree pose
                # tree_pose = detect_tree_pose(left_elbow_angle,right_elbow_angle,left_knee_angle,right_knee_angle)
                # if tree_pose:
                #     cv2.putText(frame, f"Current Pose : {tree_pose}",(width - 350, 80),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)

                current_pose = detect_pose(left_elbow_angle,right_elbow_angle,left_shoulder_angle,right_shoulder_angle,left_hip_angle,right_hip_angle,left_knee_angle,right_knee_angle)
                cv2.putText(frame,f"Current Pose : {current_pose}",(width-350,40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)



            # Final output window show karo
            cv2.imshow(
                "AI-Powered Virtual Yoga Trainer - Pose Detection",
                frame
            )

            # Agar keyboard se q press ho
            # to application band kar do
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Camera release karo
    cap.release()

    # OpenCV ki sari windows close karo
    cv2.destroyAllWindows()