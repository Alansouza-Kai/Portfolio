import cv2

def apply_gray_filter(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
