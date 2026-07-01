

def detect_t_pose(left_elbow,right_elbow,left_shoulder,right_shoulder,left_hip,right_hip):
    if (left_elbow >= 160 and right_elbow >= 160 and 80 <= left_shoulder <= 100 and 80 <= right_shoulder <= 100 and left_hip>160 and right_hip>160):
        return True
    else:
        return False


def detect_tree_pose(left_elbow,right_elbow,left_knee,right_knee,left_hip,right_hip):
    # Left Leg Tree Pose
    left_tree = (left_elbow > 160 and right_elbow > 160 and left_knee > 160 and right_knee < 120 and 90<= left_hip <= 150 and right_hip>160)

    # Right Leg Tree Pose
    right_tree = (left_elbow > 160 and right_elbow > 160 and right_knee > 160 and left_knee < 120 and 90<= right_hip <= 150 and left_hip>160)
    if left_tree:
        return "Tree Pose (Left)"

    elif right_tree:
        return "Tree Pose (Right)"

    return None

def detect_pose(left_elbow,right_elbow,left_shoulder,right_shoulder,left_hip,right_hip,left_knee,right_knee):
    t_pose=detect_t_pose(left_elbow,right_elbow,left_shoulder,right_shoulder,left_hip,right_hip)
    if t_pose:
        return "T Pose"
    tree = detect_tree_pose(left_elbow,right_elbow,left_knee,right_knee,left_hip,right_hip)

    if tree:
        return tree
    else:
        return "Unknown"

