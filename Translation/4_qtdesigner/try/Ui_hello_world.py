# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\GitHubStorage\Course_and_Learning_resource\software_learning\4_qtdesigner\hello world.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(469, 429)
        self.CaptionLabel = CaptionLabel(Frame)
        self.CaptionLabel.setGeometry(QtCore.QRect(20, 50, 70, 16))
        self.CaptionLabel.setObjectName("CaptionLabel")
        self.LineEdit = LineEdit(Frame)
        self.LineEdit.setGeometry(QtCore.QRect(10, 90, 128, 33))
        self.LineEdit.setObjectName("LineEdit")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.CaptionLabel.setText(_translate("Frame", "hello world"))
from qfluentwidgets import CaptionLabel, LineEdit
