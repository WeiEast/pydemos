# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Tue Aug 26 18:27:54 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(233, 625)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.labeltime = QtWidgets.QLabel(Form)
        self.labeltime.setObjectName("labeltime")
        self.horizontalLayout.addWidget(self.labeltime)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.labelxuan = QtWidgets.QLabel(Form)
        self.labelxuan.setAlignment(QtCore.Qt.AlignCenter)
        self.labelxuan.setObjectName("labelxuan")
        self.gridLayout.addWidget(self.labelxuan, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.pushButton, self.listWidget)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "迅雷会员帐号获取"))
        self.label.setText(_translate("Form", "帐号更新日期："))
        self.labeltime.setText(_translate("Form", "日期"))
        self.label_3.setText(_translate("Form", "↓当前选中帐号↓"))
        self.labelxuan.setText(_translate("Form", "未选中"))
        self.pushButton.setText(_translate("Form", "随机选择自动填充(F2)"))
        self.pushButton.setShortcut(_translate("Form", "F2"))
        self.label_5.setText(_translate("Form", "帮助：脚本开启后，选中列表中的帐号密码，在密码输入框按F1自动填写密码，F3结束小工具"))

