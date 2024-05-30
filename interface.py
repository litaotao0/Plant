# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import os

from PyQt5.QtWidgets import QFileDialog

import test
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import numpy as np

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(509, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 30, 121, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 80, 291, 271))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(110, 390, 261, 41))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.open_file)

    def open_file(self):
        # m = QtWidgets.QFileDialog.getExistingDirectory(None, '选取文件夹', 'C:/')
        # self.fileT.setText(m)
        imgName, imgType = QFileDialog.getOpenFileName(self.centralwidget, "打开图片", "","*.jpg;;*.png;;All Files(*)")  # 弹出一个文件选择框，第一个返回值imgName记录选中的文件路径+文件名，第二个返回值imgType记录文件的类型
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长款
        # self.label.setPixmap(QPixmap(jpg))
        jpg2 = Image.open(imgName)
        imag = jpg2.resize([64, 64])
        image = np.array(imag)
        b = test.evaluate_one_image(image)
        self.textBrowser.setText(b)
        self.label.setPixmap(jpg)  # 在label控件上显示选择的图片



    # def xuanze(self):
    #     img = Image.open('flowers/1.jpg')
    #     path = 'flowers/1.jpg'
    #     self.label.setPixmap(QPixmap(path))
    #     imag = img.resize([64, 64])
    #     image = np.array(imag)
    #     b = test.evaluate_one_image(image)
    #     # a = 'grfjhduj'
    #     self.textBrowser.setText(b)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "植物识别系统"))
        self.pushButton.setText(_translate("MainWindow", "选择一张植物图片"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # app.setWindowIcon(QIcon(r'F:\新建文件夹\BayesSpam-master\data\logo.ico'))
    widget = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())