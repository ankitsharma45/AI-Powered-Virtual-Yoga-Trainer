import numpy as np


def calculate_angle(a, b, c):
    a=np.array(a)
    b=np.array(b)
    c=np.array(c)

    angle1=np.degrees(np.arctan2(c[1]-b[1],c[0]-b[0]))
    angle2=np.degrees(np.arctan2(a[1]-b[1],a[0]-b[0]))
    angle=angle1-angle2
    angle=abs(angle)
    if angle>180:
        angle=360 - angle

    return angle


# Joint Angle Function

def get_joint_angle(landmarks, point1, point2, point3):

 
    # 3 landmarks ke x,y coordinate nikal rahe hain
    a = np.array([
        landmarks[point1].x,
        landmarks[point1].y
    ])

    b = np.array([
        landmarks[point2].x,
        landmarks[point2].y
    ])

    c = np.array([
        landmarks[point3].x,
        landmarks[point3].y
    ])

    # Existing function call
    return round(
        calculate_angle(
            a,
            b,
            c
        )
    )