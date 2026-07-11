import cv2
import mediapipe as mp
import pickle
import pandas as pd


MODEL_FILE = "models/yoga_pose_model.pkl"

with open(MODEL_FILE, "rb") as file:
    model = pickle.load(file)

print("Model Loaded Successfully.")

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

with mp_pose.Pose(
    static_image_mode=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as pose:
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
                    features.extend([
                        landmark.x,
                        landmark.y,
                        landmark.z,
                        landmark.visibility
                    ])

            if len(features) == 132:
                feature_df = pd.DataFrame(
                [features],
                columns=model.feature_names_in_
                )

                prediction = model.predict(feature_df)[0]
                print("Predicted Pose:", prediction)

            cv2.imshow(
                "AI-Powered Virtual Yoga Trainer - Predictor",
                frame
                )

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break
cap.release()
cv2.destroyAllWindows()
