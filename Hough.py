import cv2
import numpy as np
import matplotlib.pyplot as plt


class Hough:
    def __init__(self, img_path):
        self.path = img_path

    def line_change_detection(self):
        img = cv2.imread(self.path)
        img = cv2.GaussianBlur(img, (3, 3), 0)
        edges = cv2.Canny(img, 50, 150, apertureSize=3)
        lines = cv2.HoughLines(edges, 1, np.pi / 2, 118)
        result = img.copy()
        for i_line in lines:
            for line in i_line:
                rho = line[0]
                theta = line[1]
                if (theta < (np.pi / 4.)) or (theta > (3. * np.pi / 4.0)):  # 垂直直线
                    pt1 = (int(rho / np.cos(theta)), 0)
                    pt2 = (int((rho - result.shape[0] * np.sin(theta)) / np.cos(theta)), result.shape[0])
                    cv2.line(result, pt1, pt2, (0, 0, 255))
                else:
                    pt1 = (0, int(rho / np.sin(theta)))
                    pt2 = (result.shape[1], int((rho - result.shape[1] * np.cos(theta)) / np.sin(theta)))
                    cv2.line(result, pt1, pt2, (0, 0, 255), 1)
        cv2.imwrite('result.bmp', result)
        pic = plt.imread('result.bmp')
        plt.imshow(pic)
        plt.axis('off')
        plt.show()

    def line_change_detection_P(self):
        img = cv2.imread(self.path)
        img = cv2.GaussianBlur(img, (3, 3), 0)
        edges = cv2.Canny(img, 50, 150, apertureSize=3)
        lines = cv2.HoughLines(edges, 1, np.pi / 2, 118)
        minLineLength = 200
        maxLineGap = 15
        linesP = cv2.HoughLinesP(edges, 1, np.pi / 180, 80, minLineLength, maxLineGap)
        result_P = img.copy()
        for i_P in linesP:
            for x1, y1, x2, y2 in i_P:
                cv2.line(result_P, (x1, y1), (x2, y2), (0, 255, 0), 3)
        cv2.imwrite('result_p.bmp', result_P)
        pic = plt.imread('result_p.bmp')
        plt.imshow(pic)
        plt.axis('off')
        plt.show()
