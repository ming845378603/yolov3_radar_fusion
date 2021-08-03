# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog

from track import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 35, 480, 320))
        self.label.setText("")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(25, 440, 491, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(160, 375, 371, 20))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(520, 20, 21, 551))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_2.setFont(font)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(120, 10, 451, 20))
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 65, 141, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(720, 70, 50, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 0, 131, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(690, 10, 101, 20))
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 310, 71, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 365, 121, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 375, 31, 20))
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(720, 115, 50, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(550, 110, 161, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(720, 160, 50, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(550, 155, 161, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(550, 200, 161, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(720, 205, 50, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 260, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 260, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 380, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(660, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(530, 320, 21, 20))
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(620, 320, 171, 20))
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(550, 440, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(660, 440, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(600, 500, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 400, 471, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 0, 81, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(10, 10, 41, 20))
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(0, 20, 21, 551))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_9.setFont(font)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(780, 20, 21, 551))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_10.setFont(font)
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(10, 560, 781, 20))
        self.line_11.setLineWidth(3)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # by myself
        # 建立按钮的响应函数
        self.pushButton_3.clicked.connect(self.read_btn)
        self.pushButton_4.clicked.connect(self.update_btn)
        self.pushButton_6.clicked.connect(self.open_btn)
        self.pushButton_7.clicked.connect(self.playback_btn)
        self.pushButton_8.clicked.connect(self.start_btn)
        self.pushButton_9.clicked.connect(self.stop_btn)
        self.pushButton_10.clicked.connect(self.fastShot_btn)

        self.modelFlag = 0
        self.stopFlag = 0
        self.num = 0
        self.frameNum = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "智能交通视频监控系统"))
        self.label_2.setText(_translate("MainWindow", "检测置信度阈值："))
        self.label_3.setText(_translate("MainWindow", "参数设置区"))
        self.label_4.setText(_translate("MainWindow", "操作区"))
        self.label_5.setText(_translate("MainWindow", "结果显示区"))
        self.label_6.setText(_translate("MainWindow", "最小启动帧数："))
        self.label_7.setText(_translate("MainWindow", "最大允许丢失帧数："))
        self.label_8.setText(_translate("MainWindow", "IOU匹配阈值："))
        self.pushButton_3.setText(_translate("MainWindow", "读取"))
        self.pushButton_4.setText(_translate("MainWindow", "修改"))
        self.pushButton_6.setText(_translate("MainWindow", "Open"))
        self.pushButton_7.setText(_translate("MainWindow", "Playback"))
        self.pushButton_8.setText(_translate("MainWindow", "开始"))
        self.pushButton_9.setText(_translate("MainWindow", "暂停"))
        self.pushButton_10.setText(_translate("MainWindow", "快照"))
        self.label_9.setText(_translate("MainWindow", "当前帧数         运行状态        当前路况         异常情况"))
        self.label_10.setText(_translate("MainWindow", "监控区"))

    # “读取”:pushButton_3
    def read_btn(self):
        args = parse_args()
        self.lineEdit.setText(str(args.det_conf_thresh))
        self.lineEdit_2.setText(str(args.sort_min_hit))
        self.lineEdit_3.setText(str(args.sort_max_age))
        self.lineEdit_4.setText(str(0.4))

    # “更新”:pushButton_4
    def update_btn(self):
        relay = QMessageBox.question(self.pushButton_4,
                                     "参数修改",
                                     "确认调整相关参数？",
                                     QMessageBox.Yes | QMessageBox.No)
        if relay == QMessageBox.Yes:
            if self.lineEdit.text() == "" or self.lineEdit_2.text() == "" or self.lineEdit_3.text() == "" or self.lineEdit_4.text() == "":
                QMessageBox.warning(self.pushButton_4, "信息提示框", "参数不能为空！")
            else:
                QMessageBox.warning(self.pushButton_4, "信息提示框", "修改成功！")

    # “Open”:pushButton_6
    def open_btn(self):
        self.fileName, self.fileType = QFileDialog.getOpenFileName(MainWindow, 'Choose file', '', '*.avi;;*.mp4')
        if self.fileName != "":
            self.cap = cv2.VideoCapture(self.fileName)
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)
            ret, self.frame = self.cap.read()
            # 调整尺寸
            showFirst = cv2.resize(self.frame, (480, 320))
            # RGB转BGR
            showFirst = cv2.cvtColor(showFirst, cv2.COLOR_BGR2RGB)
            showImageFirst = QImage(showFirst.data, showFirst.shape[1], showFirst.shape[0], QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(showImageFirst))  # 在Label标签上显示图像
            self.modelFlag = 0

    # “Playbck”:pushButton_7
    def playback_btn(self):
        self.fileName, self.fileType = QFileDialog.getOpenFileName(MainWindow, 'Choose file', '', '*.avi;;*.mp4')
        if self.fileName != "":
            self.cap = cv2.VideoCapture(self.fileName)
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)
            ret, self.frame = self.cap.read()
            # 调整尺寸
            showFirst = cv2.resize(self.frame, (480, 320))
            # RGB转BGR
            showFirst = cv2.cvtColor(showFirst, cv2.COLOR_BGR2RGB)
            showImageFirst = QImage(showFirst.data, showFirst.shape[1], showFirst.shape[0], QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(showImageFirst))  # 在Label标签上显示图像
            self.modelFlag = 1

    # “暂停”:pushButton_9
    def stop_btn(self):
        self.stopFlag = 1

    # “快照”:pushButton_10
    def fastShot_btn(self):
        self.num += 1
        ret, self.frame = self.cap.read()
        outputFile = 'images/' + str(self.num) + '.jpg'
        cv2.imwrite(outputFile, self.frame)
        QMessageBox.warning(self.pushButton_10, "信息提示框", "快照成功，已存入设定文件夹！")

    # “开始”:pushButton_8
    def start_btn(self):
        while True:
            # 从视频流中读取一张图像，ret为读取成功/失败标识，frame为当前视频帧
            ret, self.frame = self.cap.read()
            print(ret)

            if ret == True:
                self.frameNum += 1
                # 调整尺寸
                show = cv2.resize(self.frame, (480, 320))
                # RGB转BGR
                show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
                showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                self.label.setPixmap(QPixmap.fromImage(showImage))  # 在Label标签上显示图像

                """"模式选择"""
                if self.modelFlag == 0:
                    # 间隔Xms，播放下一帧。或者按'esc'键退出，它的ASCII码为27
                    if cv2.waitKey(500) & 0xff == 27:
                        break
                else:
                    # 间隔Xms，播放下一帧。或者按'esc'键退出，它的ASCII码为27
                    if cv2.waitKey(50) & 0xff == 27:
                        break
                """"结果展示"""
                if self.stopFlag == 1:
                    state = "暂停"
                else:
                    state = "正常"
                self.textBrowser.append(
                        "   %d                 " % (self.frameNum) + state + "               正常                无")

                """暂停"""
                if self.stopFlag == 1:
                    self.stopFlag = 0
                    break

            else:
                print("Done processing !!!")
                # 释放视频流
                self.cap.release()
                break


# 线程类
class WriteThread(QtCore.QThread):
    _signal = pyqtSignal(str)

    def __init__(self):
        super(WriteThread, self).__init__()

    def run(self):
        self._signal.emit("ok")  # 发射信号

    def callback(self, msg):
        self._signal.emit(msg)  # 发射信号


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)  # 对话框初始化
    MainWindow.show()  # 显示对话框
    sys.exit(app.exec_())  # 退出
