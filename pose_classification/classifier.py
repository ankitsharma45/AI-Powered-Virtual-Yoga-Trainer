



def classify_joint(angle, straight=160, bent=80):
    if angle > straight:
        return "Straight"
    elif angle >= bent:
        return "Correct"
    else:
        return "Bent"