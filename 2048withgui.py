# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\DevFiles\eric\2048game\game.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import pyHook
import pythoncom
import win32api
import sys


class MainBody(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(703, 687)
        Dialog.setStyleSheet("*{background-color: rgb(170, 170, 0);}\n"
                             "\n"
                             "QLCDNumber\n"
                             "{\n"
                             "    border-radius:5px;\n"
                             "    background-color: rgb(170, 170, 127);\n"
                             "    color: rgb(255, 255, 255);\n"
                             "    text-align:center\n"
                             "    \n"
                             "}")
        Dialog.setSizeGripEnabled(True)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 150, 501, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.gridLayout.addWidget(self.lcdNumber_1, 0, 1, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 0, 2, 1, 1)
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.gridLayout.addWidget(self.lcdNumber_6, 1, 2, 1, 1)
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.gridLayout.addWidget(self.lcdNumber_8, 1, 4, 1, 1)
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.gridLayout.addWidget(self.lcdNumber_5, 1, 1, 1, 1)
        self.lcdNumber_9 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_9.setObjectName("lcdNumber_9")
        self.gridLayout.addWidget(self.lcdNumber_9, 2, 1, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout.addWidget(self.lcdNumber_3, 0, 3, 1, 1)
        self.lcdNumber_10 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_10.setObjectName("lcdNumber_10")
        self.gridLayout.addWidget(self.lcdNumber_10, 2, 2, 1, 1)
        self.lcdNumber_11 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_11.setObjectName("lcdNumber_11")
        self.gridLayout.addWidget(self.lcdNumber_11, 2, 3, 1, 1)
        self.lcdNumber_12 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_12.setObjectName("lcdNumber_12")
        self.gridLayout.addWidget(self.lcdNumber_12, 2, 4, 1, 1)
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.gridLayout.addWidget(self.lcdNumber_7, 1, 3, 1, 1)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_4.setStyleSheet("")
        self.lcdNumber_4.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_4.setProperty("intValue", 0)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.gridLayout.addWidget(self.lcdNumber_4, 0, 4, 1, 1)
        self.lcdNumber_13 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_13.setObjectName("lcdNumber_13")
        self.gridLayout.addWidget(self.lcdNumber_13, 3, 1, 1, 1)
        self.lcdNumber_14 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_14.setObjectName("lcdNumber_14")
        self.gridLayout.addWidget(self.lcdNumber_14, 3, 2, 1, 1)
        self.lcdNumber_15 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_15.setObjectName("lcdNumber_15")
        self.gridLayout.addWidget(self.lcdNumber_15, 3, 3, 1, 1)
        self.lcdNumber_16 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_16.setObjectName("lcdNumber_16")
        self.gridLayout.addWidget(self.lcdNumber_16, 3, 4, 1, 1)
        self.round = QtWidgets.QLabel(Dialog)
        self.round.setGeometry(QtCore.QRect(100, 70, 222, 51))
        self.table = [[self.lcdNumber_1, self.lcdNumber_2, self.lcdNumber_3, self.lcdNumber_4],
                      [self.lcdNumber_5, self.lcdNumber_6, self.lcdNumber_7, self.lcdNumber_8],
                      [self.lcdNumber_9, self.lcdNumber_10, self.lcdNumber_11, self.lcdNumber_12],
                      [self.lcdNumber_13, self.lcdNumber_14, self.lcdNumber_15, self.lcdNumber_16]]
        self.round.setStyleSheet("*\n"
                                 "{\n"
                                 "    \n"
                                 "    color:rgb(85, 85, 0);\n"
                                 "    font: 18pt \"微软雅黑\";\n"
                                 "    \n"
                                 "}")
        self.round.setObjectName("round")
        self.score = QtWidgets.QLabel(Dialog)
        self.score.setGeometry(QtCore.QRect(490, 70, 181, 51))
        self.score.setStyleSheet("*{\n"
                                 "    color:rgb(85, 85, 0);\n"
                                 "    font: 18pt \"微软雅黑\";\n"
                                 "}")
        self.score.setObjectName("score")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        print("回合" + str(self.roundnum))
        self.round.setText(_translate("Dialog", "第" + str(self.roundnum) + "回合"))
        self.score.setText(_translate("Dialog", "分数：" + str(self.scorenum)))

    def __init__(self, xnum=4, ynum=4):
        self.xnum = xnum
        self.ynum = ynum
        # 分数
        self.scorenum = 0
        # 创建棋盘
        self.data = [[0 for j in range(0, xnum)] for i in range(0, ynum)]
        # 回合数
        self.roundnum = 0
        # 每回合出现的随机数字列表
        self.randNumber = [2, 4]
        # 每回合出现的随机数字
        self.thisData = 0
        # 判断棋盘是否还有‘有效移动’
        self.flag = True
        # 赢or输
        self.fin = False
        # 是否能移动
        self.ismoved = True

    # 转置棋盘
    def trans(self):
        self.data = [[row[i] for row in self.data] for i in range(self.xnum)]

    # 刷新棋盘
    def refreshboard(self):

        # 生成随机数
        self.thisData = random.choice(self.randNumber)
        # 存放0的坐标
        zero = []

        # 每次棋盘刷新，默认没有有效移动（后面判断）
        self.flag = False

        # 把0的位置存储下来(顺便判断是否赢了以及是否有有效移动)
        for i in range(self.xnum):
            for j in range(self.ynum):
                # 判断是否胜利
                if self.data[i][j] == 2048:
                    self.fin = True
                    win32api.PostQuitMessage()
                # 判断是否还有‘有效移动’
                if i < self.xnum - 1 and j < self.xnum - 1:
                    if self.data[i][j] == self.data[i][j + 1] or self.data[i][j] == self.data[i + 1][j]:
                        self.flag = True
                # 存储0的坐标
                if self.data[i][j] == 0:
                    zero.append((i, j))

        # 如果没有0并且没有'有效移动'则gameover
        if len(zero) == 0:
            if not self.flag:
                self.fin = False
                win32api.PostQuitMessage()

        elif len(zero) != 0:
            # 判断能否移动
            if self.ismoved == False and self.roundnum > 0:
                return
            # 从zero中随机选出一个坐标，该坐标对应的值为thisData
            ranC = random.choice(zero)
            self.data[ranC[0]][ranC[1]] = self.thisData
        # 输出矩阵
        self.roundnum += 1
        # print("===========回合数：" + str(self.round) + "============")
        self.round.setText("回合数：" + str(self.roundnum))
        self.score.setText("分数：" + str(self.scorenum))
        for i in range(self.xnum):
            for j in range(self.ynum):
                self.table[i][j].setProperty("intValue", self.data[i][j])
                # print("\n")
                # print("===========分数：" + str(self.score) + "============")

    def child(self):
        self.alert = Alert()
        self.alert.show()

    # 接受子窗口的值
    @QtCore.pyqtSlot(str)
    def receive(self, s):
        print('接受到子窗口值')
        print(s)

    # 对齐
    def align(self, listdata, dir):
        count = listdata.count(0)
        # 清除所有0节点
        for i in range(count):
            listdata.remove(0)
        if dir == "left":
            # 末尾补0
            for i in range(count):
                listdata.append(0)
        elif dir == "right":
            for i in range(count):
                listdata.insert(0, 0)

    # 向左加
    def addtoleft(self):
        self.ismoved = False
        for list in self.data:
            for j in range(self.ynum - 1):
                for m in range(j + 1, self.ynum):
                    if list[j] == list[m] != 0:
                        list[j] *= 2
                        list[m] = 0
                        self.scorenum += list[j]
                        self.ismoved = True
                        break
                    elif list[j] == 0 and list[m] != 0:
                        self.ismoved = True
                        break
                    elif list[m] != 0 or list[j] == 0:
                        break
            self.align(list, "left")

    # 向右加
    def addtoright(self):
        self.ismoved = False
        for list in self.data:
            for j in range(self.ynum - 1, 0, -1):
                for m in range(j - 1, -1, -1):
                    if list[j] == list[m] != 0:
                        list[j] *= 2
                        list[m] = 0
                        self.scorenum += list[j]
                        self.ismoved = True
                        break
                    elif list[j] == 0 and list[m] != 0:
                        self.ismoved = True
                        break
                    elif list[m] != 0 or list[j] == 0:
                        break
            self.align(list, "right")

    # 按键监听
    def onKeyboardEvent(self, event):

        key = event.Key

        if key == "Up":
            self.trans()
            self.addtoleft()
            self.trans()
            self.refreshboard()

        elif key == "Left":
            self.addtoleft()
            self.refreshboard()

        elif key == "Right":
            self.addtoright()
            self.refreshboard()

        elif key == "Down":
            self.trans()
            self.addtoright()
            self.trans()
            self.refreshboard()

        return True

    # 主函数

    def main(self):
        self.refreshboard()

        # 创建一个“钩子”管理对象
        hm = pyHook.HookManager()
        # 监听所有键盘事件
        hm.KeyDown = self.onKeyboardEvent
        # 设置键盘“钩子”
        hm.HookKeyboard()
        # 进入循环，如不手动关闭，程序将一直处于监听状态
        pythoncom.PumpMessages()


class Alert(object):
    def __init__(self, message="很遗憾！你输了"):
        self.message = message

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(419, 173)
        Dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 20, 211, 51))
        self.label.setStyleSheet("*{\n"
                                 "    \n"
                                 "    font: 75 20pt \"微软雅黑\";\n"
                                 "}")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.prclose)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", self.message))
        self.pushButton.setText(_translate("Dialog", "确定"))

    def prclose(self):
        sys.exit(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    mb = MainBody()
    mb.setupUi(Dialog)
    Dialog.show()
    mb.main()

    Dialog = QtWidgets.QDialog()

    al = Alert() if mb.fin == False else Alert("恭喜你，赢了！")
    al.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
