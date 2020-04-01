import cv2
import numpy as np


def chose_morphology_method(img, kernel, type):
    if type == 'e':
        return cv2.erode(img, kernel, iterations=1)
    elif type == 'd':
        return cv2.dilate(img, kernel, iterations=1)
    elif type == 'o':
        return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    elif type == 'c':
        return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    elif type == 'g':
        return cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    elif type == 't':
        return cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    elif type == 'b':
        return cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    else:
        return img


def chose_kernel(type_ker, size):
    if type_ker == 'r':
        return cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    elif type_ker == 'e':
        return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size, size))
    elif type_ker == 'c':
        return cv2.getStructuringElement(cv2.MORPH_CROSS, (size, size))
    else:
        return np.ones((3, 3), np.uint8)
