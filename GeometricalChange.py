import cv2
import numpy as np


class GeoChange:
    def __init__(self, imgPath):
        self.path = imgPath

    def extend(self, size):
        img = cv2.imread(self.path)
        img = cv2.resize(img, (0, 0), fx=size, fy=size, interpolation=cv2.INTER_LINEAR)
        cv2.imwrite("size.bmp", img)

    def move(self, x, y):
        img = cv2.imread(self.path)
        height, width, channel = img.shape
        # 构建平移矩阵
        matrix = np.float32([[1, 0, x], [0, 1, y]])
        img = cv2.warpAffine(img, matrix, (width, height))
        cv2.imwrite("move.bmp", img)

    def horizon_flip(self):
        img = cv2.imread(self.path)
        horizon = cv2.flip(img, 1, dst=None)
        cv2.imwrite("horizon.bmp", horizon)

    def vertical_flip(self):
        img = cv2.imread(self.path)
        vertical = cv2.flip(img, 0, dst=None)
        cv2.imwrite("vertical.bmp", vertical)

    def rotation(self, degree):
        img = cv2.imread(self.path)
        rows, cols, depth = img.shape
        matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), degree, 1)
        img = cv2.warpAffine(img, matrix, (cols, rows))
        cv2.imwrite("rotation.bmp", img)

    def affine(self):

        src = cv2.imread(self.path)
        src = cv2.resize(src, (256, 256))
        rows, cols = src.shape[: 2]
        post1 = np.float32([[50, 50], [200, 50], [50, 200]])
        post2 = np.float32([[10, 100], [200, 50], [100, 250]])
        M = cv2.getAffineTransform(post1, post2)
        result = cv2.warpAffine(src, M, (rows, cols))
        cv2.imwrite("affine.bmp", result)
