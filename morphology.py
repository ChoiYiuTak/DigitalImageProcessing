import cv2
import numpy as np


class morphology:
    def __init__(self, img_path):
        self.path = img_path

    def corrode(self):
        src = cv2.imread(self.path, cv2.IMREAD_UNCHANGED)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
        erosion = cv2.erode(src, kernel)
        cv2.imwrite("erosion.bmp", erosion)
