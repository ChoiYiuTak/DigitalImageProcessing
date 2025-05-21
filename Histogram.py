import cv2
import matplotlib.pyplot as plt
import numpy as np


class Histogram:
    def __init__(self, img_path):
        self.path = img_path

    def histGrey(self):
        img1 = cv2.imread(self.path)
        img = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
        hist = cv2.calcHist([img], [0], None, [256], [0, 255])
        plt.plot(hist)
        plt.xlim([0, 255])
        plt.show()

    def histRGB(self):
        src = cv2.imread(self.path)
        color = ["r", "g", "b"]
        b, g, r = cv2.split(src)
        src = cv2.merge([r, g, b])
        for index, c in enumerate(color):
            hist = cv2.calcHist([src], [index], None, [256], [0, 255])
            plt.plot(hist, color=c)
            plt.xlim([0, 255])
        plt.show()

    def hist(self):
        src = cv2.imread(self.path)
        b, g, r = cv2.split(src)
        src = cv2.merge([r, g, b])
        histr = cv2.calcHist([src], [0], None, [256], [0, 256])
        plt.plot(histr, color='r')
        plt.xlim([0, 256])
        histr = cv2.calcHist([src], [1], None, [256], [0, 256])
        plt.plot(histr, color='g')
        plt.xlim([0, 256])
        histr = cv2.calcHist([src], [2], None, [256], [0, 256])
        plt.plot(histr, color='b')
        plt.xlim([0, 256])
        plt.show()

    def editHist(self):
        img = cv2.imread(self.path, 0)
        h, w = img.shape[:2]
        out = np.zeros(img.shape, np.uint8)
        for i in range(h):
            for j in range(w):
                pix = img[i][j]
                if pix < 50:
                    out[i][j] = 0.5 * pix
                elif pix < 150:
                    out[i][j] = 3.6 * pix - 310
                else:
                    out[i][j] = 0.238 * pix + 194
        out = np.around(out)
        out = out.astype(np.uint8)
        plt.subplot(121)
        plt.imshow(img, 'gray')
        plt.subplot(122)
        pixelSequence = img.ravel()
        numberBins = 256
        histogram, bins, patch = plt.hist(pixelSequence, numberBins)
        plt.axis([0, 255, 0, np.max(histogram)])
        plt.show()
        plt.subplot(121)
        plt.imshow(out, 'gray')
        plt.subplot(122)
        pixelSequence = out.ravel()
        numberBins = 256
        histogram, bins, patch = plt.hist(pixelSequence, numberBins)
        plt.axis([0, 255, 0, np.max(histogram)])
        plt.show()
