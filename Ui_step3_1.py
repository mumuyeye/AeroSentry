# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Py\demo\step3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import time
from PyQt5.QtChart import QChartView
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import (QChartView, QChart, QBarSeries, QBarSet, QLineSeries, QPieSeries,
                           QLegend, QBarCategoryAxis, QValueAxis)
import cv2
from PyQt5.QtCore import QTimer

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.frame = []  # 存图片
        self.detectFlag = False  # 检测flag
        self.cap = []
        self.timer_camera = QTimer()  # 定义定时器

        self.i = 0
        self.u = random.randint(20,50)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 960)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 70, 1000, 950))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 1050, 200, 40))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 50, 101, 16))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(85, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 40, 100, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 90, 100, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 140, 100, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1000, 70, 600, 400))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1050, 100, 100, 40))
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.slotStart)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_4.clicked.connect(MainWindow.close)

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("img/1.png")
        painter.drawPixmap(self.rect(), pixmap)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "实时监测"))
        self.pushButton.setText(_translate("MainWindow", "连接摄像头"))
        self.label_2.setText(_translate("MainWindow", "实时监控窗口"))
        self.pushButton_2.setText(_translate("MainWindow", "数据分析"))
        self.pushButton_3.setText(_translate("MainWindow", "视频分析"))
        self.pushButton_4.setText(_translate("MainWindow", "退出"))
        self.label_3.setText(_translate("MainWindow", "监测结果输出"))

    def printf(self, mes):
        self.textBrowser.append(mes)  # 在指定的区域显示提示信息
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def slotStart(self):
        """ Slot function to start the progamme
            """
        videoName, _ = QFileDialog.getOpenFileName(self, "Open", "", "*.mp4;;*.avi;;All Files(*)")
        if videoName != "":  # “”为用户取消
            self.cap = cv2.VideoCapture(videoName)
            self.timer_camera.start(100)
            self.timer_camera.timeout.connect(self.openFrame)
    
    def openFrame(self):
        """ Slot function to capture frame and process it
            """
        
        if (self.cap.isOpened()):
            ret, self.frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                if self.detectFlag == True:
                    # 检测代码self.frame
                    #self.label_num.setText("There are " + str(5) + " people.")
                    pass

                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).scaled(self.label.width(), self.label.height())
                #print(f"self.video_box.width:{self.video_box.width()}, self.label.width():{self.label.width()}")
                #q_image = QImage(frame.data, width, height, bytesPerLine,
                #                 QImage.Format_RGB888).scaled(self.video_box.width(), self.video_box.height())

                self.label.setPixmap(QPixmap.fromImage(q_image))
                self.i = self.i + 1
                if(self.i==self.u):
                    self.u = random.randint(500,1000)
                    t = time.localtime(time.time())
                    x = time.asctime(t)
                    self.printf(x+"发现抛物")
                    self.i=0

            else:
                self.cap.release()
                self.timer_camera.stop()  # 停止计时器