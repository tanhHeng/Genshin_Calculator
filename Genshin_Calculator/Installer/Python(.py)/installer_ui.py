# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installer_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, installer):
        installer.setObjectName("installer")
        installer.resize(400, 204)
        installer.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(installer)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 380, 151))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 170, 380, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        installer.setCentralWidget(self.centralwidget)

        self.retranslateUi(installer)
        QtCore.QMetaObject.connectSlotsByName(installer)

    def retranslateUi(self, installer):
        _translate = QtCore.QCoreApplication.translate
        installer.setWindowTitle(_translate("installer", "installer"))

