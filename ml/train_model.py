import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix )
import pickle
import os
import cv2

df = pd.read_csv("dataset/yoga_pose_dataset.csv")
# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.info()) # check no of rows and column
# print(df["pose"].value_counts())

X = df.drop("pose", axis=1) # create feature data pose column ko drop karke

y =df["pose"]

# print("X Shape:", X.shape)
# print("y Shape:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# print("X Train Shape:", X_train.shape)
# print("X Test Shape:", X_test.shape)
# print("y Train Shape:", y_train.shape)
# print("y Test Shape:", y_test.shape)

#model utha liya
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
# print("Model Training Completed Successfully.")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Model Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nAccuracy:")
print(f"Model Accuracy: {accuracy * 100:.2f}%")



MODEL_DIR = "models"

os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_FILE = "models/yoga_pose_model.pkl"

with open(MODEL_FILE, "wb") as file:
    pickle.dump(model, file)

print(f"Model saved successfully at: {MODEL_FILE}")

