import cv2

def read_image(path):
    return cv2.imread(path)

def save_image(path, image):
    cv2.imwrite(path, image)
