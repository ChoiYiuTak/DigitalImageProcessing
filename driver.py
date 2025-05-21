import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from DIP import Ui_DigitalImageProcessing
from GeometricalChange import GeoChange
from LogicalAlgorithm import logicalAlgorithm
from Histogram import Histogram
from Hough import Hough
from EdgeDetection import edgeDetect
from morphology import morphology


class run(QtWidgets.QMainWindow, Ui_DigitalImageProcessing):

    def __init__(self):
        super(run, self).__init__()
        self.setupUi(self)
        # 原图像路径，后面将作为图像处理的参数，表示对哪张图片进行图像处理。
        self.img_path = ""

    # 打开图像函数
    def openImg(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "Open image", "", "All Files(*);")
        self.img_path = imgName
        jpg = QtGui.QPixmap(imgName).scaled(self.original_img.width(), self.original_img.height())
        self.original_img.setPixmap(jpg)

    # 展示修改后图片
    def showImg(self, pic_path):
        jpg = QtGui.QPixmap(pic_path).scaled(self.original_img.width(), self.original_img.height())
        self.fixed_img.setPixmap(jpg)

    # 此处开始处理图像逻辑运算的槽函数, alAnd为图像与操作
    def alAnd(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "All Files(*);")
        al = logicalAlgorithm(self.img_path, imgName)
        al.alAnd()
        self.showImg("And.bmp")

    # 图像或操作槽函数
    def alOr(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "All Files(*);")
        al = logicalAlgorithm(self.img_path, imgName)
        al.alOr()
        self.showImg("Or.bmp")

    # 图像非操作槽函数
    def alNegation(self):
        al = logicalAlgorithm(self.img_path, self.img_path)
        al.alNegation()
        self.showImg("Negation.bmp")

    # 图像加法操作槽函数
    def alAdd(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "All Files(*);")
        al = logicalAlgorithm(self.img_path, imgName)
        al.alAdd()
        self.showImg("Add.bmp")

    # 图像减法操作槽函数
    def alSubtract(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "All Files(*);")
        al = logicalAlgorithm(self.img_path, imgName)
        al.alSubtract()
        self.showImg("Subtract.bmp")

    # 图像乘法操作槽函数
    def alMulty(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "All Files(*);")
        al = logicalAlgorithm(self.img_path, imgName)
        al.alMulty()
        self.showImg("Multiply.bmp")

    # 图像除法操作槽函数
    def alDivide(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "All Files(*);")
        al = logicalAlgorithm(self.img_path, imgName)
        al.alDivide()
        self.showImg("Divide.bmp")

    # 此处开始处理图像几何变化的槽函数，extend是图像放缩槽函数
    def extend(self):
        size, _ = QInputDialog.getText(self, "放缩倍数", "请输入放缩倍数, 倍数应为非负数。\n由于修改后图片预览是固定大小的，因此无法体现放缩效果\n请前往图片保存地址进行查看。", QLineEdit.Normal, "2")
        try:
            size = float(size)
            geo = GeoChange(self.img_path)
            geo.extend(size)
            self.showImg("size.bmp")
        except Exception as error:
            QMessageBox.about(self.window(), "提示", f"{error}\n输入有误！请检查输入格式与内容。")

    # 图像平移槽函数
    def moveImg(self):
        xny, _ = QInputDialog.getText(self, "平移参数", "请输入平移参数\n输入格式为a,b其中a与b以英文逗号隔开。\n", QLineEdit.Normal, "20,20")
        try:
            ipt = xny.split(",")
            a, b = [float(x) for x in ipt]
            geo = GeoChange(self.img_path)
            geo.move(a, b)
            self.showImg("move.bmp")
        except Exception as error:
            QMessageBox.about(self.window(), "提示", f"{error}\n输入有误!请检查输入格式与内容。")

    # 图像旋转槽函数
    def rotation(self):
        degree, _ = QInputDialog.getText(self, "旋转角度", "请输入旋转角度，角度应为实数", QLineEdit.Normal, "90")
        try:
            degree = float(degree)
            geo = GeoChange(self.img_path)
            geo.rotation(degree)
            self.showImg("rotation.bmp")
        except Exception as error:
            QMessageBox.about(self.window(), "提示", f"{error}\n输入有误!请检查输入格式与内容。")

    # 图像水平翻折槽函数
    def horizonal(self):
        geo = GeoChange(self.img_path)
        geo.horizon_flip()
        self.showImg("horizon.bmp")

    # 图像垂直翻折槽函数
    def vertical(self):
        geo = GeoChange(self.img_path)
        geo.vertical_flip()
        self.showImg("vertical.bmp")

    # 仿射变换槽函数
    def affine(self):
        geo = GeoChange(self.img_path)
        geo.affine()
        self.showImg("affine.bmp")

    # 下面开始对数字图像的直方图进行绘制，histGrey为绘制灰度直方图的槽函数
    def histGrey(self):
        hist = Histogram(self.img_path)
        hist.histGrey()
        self.showImg(self.img_path)

    # 彩色直方图绘制
    def histRGB(self):
        hist = Histogram(self.img_path)
        hist.histRGB()
        self.showImg(self.img_path)

    # 绘制直方图
    def histD(self):
        hist = Histogram(self.img_path)
        hist.hist()
        self.showImg(self.img_path)

    # 修改灰度直方图
    def editHist(self):
        hist = Histogram(self.img_path)
        hist.editHist()
        self.showImg(self.img_path)

    # 以下是使用opencv实现线条变化检测的函数
    def houghLines(self):
        hough = Hough(self.img_path)
        hough.line_change_detection()
        self.showImg("result.bmp")

    # 使用Hough P实现线条变化检测
    def houghLinesP(self):
        hough = Hough(self.img_path)
        hough.line_change_detection_P()
        self.showImg('result_p.bmp')

    # 图像边缘检测部分
    def basic_of_edge_detection(self):
        edge = edgeDetect(self.img_path)
        edge.graphicsEnhance()
        self.showImg('sharp.bmp')

    # Roberts算子
    def roberts(self):
        edge = edgeDetect(self.img_path)
        edge.roberts()
        self.showImg("roberts.bmp")

    # Prewitt & sobel
    def sobel(self):
        edge = edgeDetect(self.img_path)
        edge.sobel()
        self.showImg("sobel.bmp")

    # laplacian
    def laplacian(self):
        edge = edgeDetect(self.img_path)
        edge.laplacian()
        self.showImg("laplacian.bmp")

    # LoG
    def LoG(self):
        edge = edgeDetect(self.img_path)
        edge.LoG()
        self.showImg("log.bmp")

    # canny
    def canny(self):
        edge = edgeDetect(self.img_path)
        edge.canny()
        self.showImg("edge_output.bmp")

    # 以下为图像形态学
    def corrode(self):
        morph = morphology(self.img_path)
        morph.corrode()
        self.showImg("erosion.bmp")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    now_Status = run()
    now_Status.show()
    sys.exit(app.exec_())
