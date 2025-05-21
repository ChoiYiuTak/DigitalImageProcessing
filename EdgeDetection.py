import cv2
import numpy as np


class edgeDetect:
    def __init__(self, imgPath):
        self.path = imgPath

    def graphicsEnhance(self):
        img_gray = cv2.imread(self.path, 0)
        h, w = img_gray.shape
        gradient = np.zeros((h, w))
        # 计算图像梯度
        img_gray = img_gray.astype('float')
        for i in range(h - 1):
            for j in range(w - 1):
                gx = abs(img_gray[i + 1, j] - img_gray[i, j])
                gy = abs(img_gray[i, j + 1] - img_gray[i, j])
                gradient[i, j] = gx + gy
        sharp = img_gray + gradient
        sharp = np.where(sharp > 255, 255, sharp)
        sharp = np.where(sharp < 0, 0, sharp)
        cv2.imwrite("sharp.bmp", sharp)

    def roberts(self):
        img = cv2.imread(self.path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
        kernely = np.array([[0, -1], [1, 0]], dtype=int)
        x = cv2.filter2D(img, cv2.CV_16S, kernelx)
        y = cv2.filter2D(img, cv2.CV_16S, kernely)
        absX = cv2.convertScaleAbs(x)
        absY = cv2.convertScaleAbs(y)
        Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
        cv2.imwrite("roberts.bmp", Roberts)

    def sobel(self):
        Sobel = cv2.imread(self.path)
        Sobel = cv2.cvtColor(Sobel, cv2.COLOR_BGR2GRAY)
        x = cv2.Sobel(Sobel, cv2.CV_16S, 1, 0)
        y = cv2.Sobel(Sobel, cv2.CV_16S, 0, 1)
        absX = cv2.convertScaleAbs(x)
        absY = cv2.convertScaleAbs(y)
        Sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
        cv2.imwrite("sobel.bmp", Sobel)

    def laplacian(self):
        img = cv2.imread(self.path)
        grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_gaussianBlur = cv2.GaussianBlur(grayImage, (5, 5), 0)
        dst = cv2.Laplacian(img_gaussianBlur, cv2.CV_16S, ksize=3)
        Laplacian = cv2.convertScaleAbs(dst)
        cv2.imwrite("laplacian.bmp", Laplacian)

    def LoG(self):
        img = cv2.imread(self.path)
        grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.copyMakeBorder(grayImage, 2, 2, 2, 2, borderType=cv2.BORDER_REPLICATE)
        img = cv2.GaussianBlur(img, (3, 3), 0, 0)
        m1 = np.array(
            [[0, 0, -1, 0, 0], [0, -1, -2, -1, 0], [-1, -2, 16, -2, -1], [0, -1, -2, -1, 0], [0, 0, -1, 0, 0]],
            dtype=np.int32)
        image1 = np.zeros(img.shape).astype(np.int32)
        h, w, _ = img.shape
        for i in range(2, h - 2):
            for j in range(2, w - 2):
                image1[i, j] = np.sum(m1 * img[i - 2:i + 3, j - 2:j + 3, 1])
        image1 = cv2.convertScaleAbs(image1)
        cv2.imwrite("log.bmp", image1)

    def canny(self):
        src = cv2.imread(self.path)
        blur = cv2.GaussianBlur(src, (3, 3), 0)
        grayImage = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        gradx = cv2.Sobel(grayImage, cv2.CV_16SC1, 1, 0)
        grady = cv2.Sobel(grayImage, cv2.CV_16SC1, 0, 1)
        edge_output = cv2.Canny(gradx, grady, 50, 150)
        cv2.imwrite("edge_output.bmp", edge_output)
