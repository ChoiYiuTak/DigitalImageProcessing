import cv2
import numpy as np


class logicalAlgorithm:
    def __init__(self, img_path1, img_path2):
        self.path1 = img_path1
        self.path2 = img_path2

    def alAnd(self):
        x = cv2.imread(self.path1, 1)
        y = cv2.imread(self.path2, 1)
        rows, cols = x.shape[:2]
        y_dst = cv2.resize(y, (cols, rows), interpolation=cv2.INTER_CUBIC)
        result = (x & y_dst)
        cv2.imwrite("And.bmp", result)

    def alOr(self):
        x = cv2.imread(self.path1, 1)
        y = cv2.imread(self.path2, 1)
        rows, cols = x.shape[:2]
        y_dst = cv2.resize(y, (cols, rows), interpolation=cv2.INTER_CUBIC)
        result = (x | y_dst)
        cv2.imwrite("Or.bmp", result)

    def alNegation(self):
        x = cv2.imread(self.path1, 1)
        result = (~x)
        cv2.imwrite("Negation.bmp", result)

    def alAdd(self):
        x = cv2.imread(self.path1, 1)
        y = cv2.imread(self.path2, 1)
        rows, cols = x.shape[:2]
        y_dst = cv2.resize(y, (cols, rows), interpolation=cv2.INTER_CUBIC)
        result = cv2.add(x, y_dst)
        cv2.imwrite("Add.bmp", result)

    def alSubtract(self):
        x = cv2.imread(self.path1, 1)
        y = cv2.imread(self.path2, 1)
        rows, cols = x.shape[:2]
        y_dst = cv2.resize(y, (cols, rows), interpolation=cv2.INTER_CUBIC)
        result = cv2.subtract(x, y_dst)
        cv2.imwrite("Subtract.bmp", result)

    def alMulty(self):
        x = cv2.imread(self.path1, 1).astype(np.float64)/255
        y = cv2.imread(self.path2, 1).astype(np.float64)/255
        rows, cols = x.shape[:2]
        y_dst = cv2.resize(y, (cols, rows), interpolation=cv2.INTER_CUBIC)
        result = cv2.multiply(x, y_dst) * 255
        cv2.imwrite("Multiply.bmp", result)

    def alDivide(self):
        x = cv2.imread(self.path1, 1).astype(np.float64)/255
        y = cv2.imread(self.path2, 1).astype(np.float64)/255
        rows, cols = x.shape[:2]
        y_dst = cv2.resize(y, (cols, rows), interpolation=cv2.INTER_CUBIC)
        result = cv2.divide(x, y_dst) * 255
        cv2.imwrite("Divide.bmp", result)
