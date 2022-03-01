# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menu = QtWidgets.QGroupBox(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(0, 140, 121, 461))
        self.menu.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px solid #dcdfe6;")
        self.menu.setObjectName("menu")
        self.menuCalculatorButton = QtWidgets.QPushButton(self.menu)
        self.menuCalculatorButton.setGeometry(QtCore.QRect(0, 0, 120, 60))
        self.menuCalculatorButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuCalculatorButton.setToolTip("")
        self.menuCalculatorButton.setWhatsThis("")
        self.menuCalculatorButton.setStyleSheet("QPushButton{\n"
"    font: 12pt \"Adobe 宋体 Std R\";\n"
"    border: 0px solid #dcdfe6;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border: 0px solid #dcdfe6;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    border: 0px solid #dcdfe6;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(200, 200, 200, 255), stop:0.05 rgba(200, 200, 200, 255), stop:0.15 rgba(230, 230, 230, 255),  stop:1 rgba(250, 250, 250, 255));\n"
"}\n"
"")
        self.menuCalculatorButton.setCheckable(True)
        self.menuCalculatorButton.setChecked(True)
        self.menuCalculatorButton.setAutoRepeat(False)
        self.menuCalculatorButton.setAutoExclusive(True)
        self.menuCalculatorButton.setAutoDefault(False)
        self.menuCalculatorButton.setObjectName("menuCalculatorButton")
        self.menuAboutButton = QtWidgets.QPushButton(self.menu)
        self.menuAboutButton.setGeometry(QtCore.QRect(0, 180, 120, 60))
        self.menuAboutButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuAboutButton.setStyleSheet("QPushButton{\n"
"    font: 12pt \"Adobe 宋体 Std R\";\n"
"    border: 0px solid #dcdfe6;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border: 0px solid #dcdfe6;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    border: 0px solid #dcdfe6;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(200, 200, 200, 255), stop:0.05 rgba(200, 200, 200, 255), stop:0.15 rgba(230, 230, 230, 255),  stop:1 rgba(250, 250, 250, 255));\n"
"}\n"
"")
        self.menuAboutButton.setCheckable(True)
        self.menuAboutButton.setAutoRepeat(False)
        self.menuAboutButton.setAutoExclusive(True)
        self.menuAboutButton.setObjectName("menuAboutButton")
        self.menuHelpButton = QtWidgets.QPushButton(self.menu)
        self.menuHelpButton.setGeometry(QtCore.QRect(0, 60, 120, 60))
        self.menuHelpButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuHelpButton.setStyleSheet("QPushButton{\n"
"    font: 12pt \"Adobe 宋体 Std R\";\n"
"    border: 0px solid #dcdfe6;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border: 0px solid #dcdfe6;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    border: 0px solid #dcdfe6;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(200, 200, 200, 255), stop:0.05 rgba(200, 200, 200, 255), stop:0.15 rgba(230, 230, 230, 255),  stop:1 rgba(250, 250, 250, 255));\n"
"}\n"
"")
        self.menuHelpButton.setCheckable(True)
        self.menuHelpButton.setChecked(False)
        self.menuHelpButton.setAutoExclusive(True)
        self.menuHelpButton.setObjectName("menuHelpButton")
        self.menuAboutButton_2 = QtWidgets.QPushButton(self.menu)
        self.menuAboutButton_2.setGeometry(QtCore.QRect(0, 120, 120, 60))
        self.menuAboutButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuAboutButton_2.setStyleSheet("QPushButton{\n"
"    font: 12pt \"Adobe 宋体 Std R\";\n"
"    border: 0px solid #dcdfe6;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border: 0px solid #dcdfe6;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    border: 0px solid #dcdfe6;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(200, 200, 200, 255), stop:0.05 rgba(200, 200, 200, 255), stop:0.15 rgba(230, 230, 230, 255),  stop:1 rgba(250, 250, 250, 255));\n"
"}\n"
"")
        self.menuAboutButton_2.setCheckable(True)
        self.menuAboutButton_2.setAutoRepeat(False)
        self.menuAboutButton_2.setAutoExclusive(True)
        self.menuAboutButton_2.setObjectName("menuAboutButton_2")
        self.menuCalculatorButton.raise_()
        self.menuHelpButton.raise_()
        self.menuAboutButton.raise_()
        self.menuAboutButton_2.raise_()
        self.main_title_1 = QtWidgets.QLabel(self.centralwidget)
        self.main_title_1.setGeometry(QtCore.QRect(0, 0, 61, 31))
        self.main_title_1.setStyleSheet("font: 16pt \"Adobe 黑体 Std R\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.main_title_1.setObjectName("main_title_1")
        self.main_title_2 = QtWidgets.QLabel(self.centralwidget)
        self.main_title_2.setGeometry(QtCore.QRect(57, 3, 61, 31))
        self.main_title_2.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.main_title_2.setObjectName("main_title_2")
        self.main_title_picture = QtWidgets.QLabel(self.centralwidget)
        self.main_title_picture.setGeometry(QtCore.QRect(25, 50, 64, 64))
        self.main_title_picture.setStyleSheet("")
        self.main_title_picture.setText("")
        self.main_title_picture.setPixmap(QtGui.QPixmap("icon-circle.png"))
        self.main_title_picture.setObjectName("main_title_picture")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(120, 0, 3, 720))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.calculatorBox = QtWidgets.QGroupBox(self.centralwidget)
        self.calculatorBox.setEnabled(True)
        self.calculatorBox.setGeometry(QtCore.QRect(139, 19, 1111, 661))
        self.calculatorBox.setAutoFillBackground(False)
        self.calculatorBox.setStyleSheet("border: 0px;")
        self.calculatorBox.setTitle("")
        self.calculatorBox.setObjectName("calculatorBox")
        self.calculatorTitle = QtWidgets.QLabel(self.calculatorBox)
        self.calculatorTitle.setGeometry(QtCore.QRect(0, 0, 111, 31))
        self.calculatorTitle.setStyleSheet("font: 16pt \"Adobe 黑体 Std R\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.calculatorTitle.setObjectName("calculatorTitle")
        self.calculatorInput = QtWidgets.QLineEdit(self.calculatorBox)
        self.calculatorInput.setGeometry(QtCore.QRect(80, 550, 1031, 31))
        self.calculatorInput.setStyleSheet("border: 1px solid #646464;\n"
"font: 25 10pt \"Adobe 宋体 Std L\";\n"
"ui->button->setFocus;\n"
"ui->button->setDefault(true);")
        self.calculatorInput.setObjectName("calculatorInput")
        self.calculatorClearButton = QtWidgets.QPushButton(self.calculatorBox)
        self.calculatorClearButton.setGeometry(QtCore.QRect(90, 0, 91, 30))
        self.calculatorClearButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculatorClearButton.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Adobe 宋体 Std R\";\n"
"    border: 2px solid #c8c8c8;\n"
"    border-radius:5px;\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(250, 250, 250);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border: 1px solid #c8c8c8;\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"")
        self.calculatorClearButton.setObjectName("calculatorClearButton")
        self.calculatorCommandLabel = QtWidgets.QLabel(self.calculatorBox)
        self.calculatorCommandLabel.setEnabled(True)
        self.calculatorCommandLabel.setGeometry(QtCore.QRect(0, 550, 81, 31))
        self.calculatorCommandLabel.setStyleSheet("border: 1px solid #646464;")
        self.calculatorCommandLabel.setObjectName("calculatorCommandLabel")
        self.calculatorCharacterInputButton = QtWidgets.QPushButton(self.calculatorBox)
        self.calculatorCharacterInputButton.setGeometry(QtCore.QRect(80, 580, 91, 31))
        self.calculatorCharacterInputButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculatorCharacterInputButton.setToolTipDuration(-1)
        self.calculatorCharacterInputButton.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Adobe 宋体 Std R\";\n"
"    border: 1px solid #646464;;\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(250, 250, 250);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border: 1px solid #646464;\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"QPushButton:Tooltip\n"
"{\n"
"    background-color: rgb(255,255,255)\n"
"}")
        self.calculatorCharacterInputButton.setObjectName("calculatorCharacterInputButton")
        self.calculatorToolsLabel = QtWidgets.QLabel(self.calculatorBox)
        self.calculatorToolsLabel.setGeometry(QtCore.QRect(0, 580, 81, 31))
        self.calculatorToolsLabel.setStyleSheet("border: 1px solid #646464;")
        self.calculatorToolsLabel.setObjectName("calculatorToolsLabel")
        self.calculatorInjButton = QtWidgets.QPushButton(self.calculatorBox)
        self.calculatorInjButton.setGeometry(QtCore.QRect(170, 580, 91, 31))
        self.calculatorInjButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculatorInjButton.setToolTipDuration(-1)
        self.calculatorInjButton.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Adobe 宋体 Std R\";\n"
"    border: 1px solid #646464;;\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(250, 250, 250);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border: 1px solid #646464;\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"QPushButton:Tooltip\n"
"{\n"
"    background-color: rgb(255,255,255)\n"
"}")
        self.calculatorInjButton.setObjectName("calculatorInjButton")
        self.calculatorHistoryButton = QtWidgets.QPushButton(self.calculatorBox)
        self.calculatorHistoryButton.setGeometry(QtCore.QRect(260, 580, 91, 31))
        self.calculatorHistoryButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculatorHistoryButton.setToolTipDuration(-1)
        self.calculatorHistoryButton.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Adobe 宋体 Std R\";\n"
"    border: 1px solid #646464;;\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(250, 250, 250);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border: 1px solid #646464;\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"QPushButton:Tooltip\n"
"{\n"
"    background-color: rgb(255,255,255)\n"
"}")
        self.calculatorHistoryButton.setObjectName("calculatorHistoryButton")
        self.calculatorShengYiWuInputButton = QtWidgets.QPushButton(self.calculatorBox)
        self.calculatorShengYiWuInputButton.setGeometry(QtCore.QRect(350, 580, 101, 31))
        self.calculatorShengYiWuInputButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculatorShengYiWuInputButton.setToolTipDuration(-1)
        self.calculatorShengYiWuInputButton.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Adobe 宋体 Std R\";\n"
"    border: 1px solid #646464;;\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(250, 250, 250);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border: 1px solid #646464;\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"QPushButton:Tooltip\n"
"{\n"
"    background-color: rgb(255,255,255)\n"
"}")
        self.calculatorShengYiWuInputButton.setObjectName("calculatorShengYiWuInputButton")
        self.calculatorShengYiWuCalButton = QtWidgets.QPushButton(self.calculatorBox)
        self.calculatorShengYiWuCalButton.setGeometry(QtCore.QRect(450, 580, 101, 31))
        self.calculatorShengYiWuCalButton.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.calculatorShengYiWuCalButton.setToolTipDuration(-1)
        self.calculatorShengYiWuCalButton.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Adobe 宋体 Std R\";\n"
"    border: 1px solid #646464;;\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(250, 250, 250);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border: 1px solid #646464;\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"QPushButton:Tooltip\n"
"{\n"
"    background-color: rgb(255,255,255)\n"
"}")
        self.calculatorShengYiWuCalButton.setObjectName("calculatorShengYiWuCalButton")
        self.calculatorToolsmakingLabel = QtWidgets.QLabel(self.calculatorBox)
        self.calculatorToolsmakingLabel.setEnabled(True)
        self.calculatorToolsmakingLabel.setGeometry(QtCore.QRect(550, 580, 561, 31))
        self.calculatorToolsmakingLabel.setAcceptDrops(False)
        self.calculatorToolsmakingLabel.setStyleSheet("border: 1px solid #646464;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.calculatorToolsmakingLabel.setObjectName("calculatorToolsmakingLabel")
        self.calculatorOutput = QtWidgets.QTextEdit(self.calculatorBox)
        self.calculatorOutput.setEnabled(True)
        self.calculatorOutput.setGeometry(QtCore.QRect(0, 40, 1111, 511))
        self.calculatorOutput.setAcceptDrops(False)
        self.calculatorOutput.setStyleSheet("border: 1px solid #646464;\n"
"font: 10pt \"Adobe 宋体 Std R\";\n"
"background-color: rgb(250, 250, 250);\n"
"ui->textEdit->moveCursor(QTextCursor::End);")
        self.calculatorOutput.setReadOnly(True)
        self.calculatorOutput.setObjectName("calculatorOutput")
        self.calculatorAutoClearCheckBox = QtWidgets.QCheckBox(self.calculatorBox)
        self.calculatorAutoClearCheckBox.setGeometry(QtCore.QRect(200, 5, 92, 20))
        self.calculatorAutoClearCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculatorAutoClearCheckBox.setObjectName("calculatorAutoClearCheckBox")
        self.tipsLabel = QtWidgets.QLineEdit(self.calculatorBox)
        self.tipsLabel.setGeometry(QtCore.QRect(0, 620, 551, 22))
        self.tipsLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tipsLabel.setAcceptDrops(False)
        self.tipsLabel.setStyleSheet("border: 0px;")
        self.tipsLabel.setReadOnly(True)
        self.tipsLabel.setObjectName("tipsLabel")
        self.calculatorOutput.raise_()
        self.calculatorCharacterInputButton.raise_()
        self.calculatorTitle.raise_()
        self.calculatorClearButton.raise_()
        self.calculatorCommandLabel.raise_()
        self.calculatorToolsLabel.raise_()
        self.calculatorInjButton.raise_()
        self.calculatorHistoryButton.raise_()
        self.calculatorShengYiWuInputButton.raise_()
        self.calculatorShengYiWuCalButton.raise_()
        self.calculatorToolsmakingLabel.raise_()
        self.calculatorInput.raise_()
        self.calculatorAutoClearCheckBox.raise_()
        self.tipsLabel.raise_()
        self.versionLabel = QtWidgets.QLineEdit(self.centralwidget)
        self.versionLabel.setGeometry(QtCore.QRect(990, 690, 291, 22))
        self.versionLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.versionLabel.setAcceptDrops(False)
        self.versionLabel.setStyleSheet("border: 0px;")
        self.versionLabel.setReadOnly(True)
        self.versionLabel.setObjectName("versionLabel")
        self.SeverBox = QtWidgets.QGroupBox(self.centralwidget)
        self.SeverBox.setGeometry(QtCore.QRect(909, 27, 341, 32))
        self.SeverBox.setStyleSheet("border: 0px;")
        self.SeverBox.setTitle("")
        self.SeverBox.setCheckable(False)
        self.SeverBox.setObjectName("SeverBox")
        self.calculatorRunSeverButton = QtWidgets.QPushButton(self.SeverBox)
        self.calculatorRunSeverButton.setGeometry(QtCore.QRect(140, 1, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std R")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.calculatorRunSeverButton.setFont(font)
        self.calculatorRunSeverButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculatorRunSeverButton.setToolTipDuration(-1)
        self.calculatorRunSeverButton.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Adobe 宋体 Std R\";\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(235, 245, 255);\n"
"    \n"
"}\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    background-color: rgb(225, 240, 255);\n"
"}\n"
"QPushButton:Tooltip\n"
"{\n"
"    background-color: rgb(255,255,255)\n"
"}")
        self.calculatorRunSeverButton.setCheckable(True)
        self.calculatorRunSeverButton.setChecked(True)
        self.calculatorRunSeverButton.setAutoExclusive(True)
        self.calculatorRunSeverButton.setObjectName("calculatorRunSeverButton")
        self.calculatorBreakSeverButton = QtWidgets.QPushButton(self.SeverBox)
        self.calculatorBreakSeverButton.setGeometry(QtCore.QRect(190, 1, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std R")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.calculatorBreakSeverButton.setFont(font)
        self.calculatorBreakSeverButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculatorBreakSeverButton.setToolTipDuration(-1)
        self.calculatorBreakSeverButton.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Adobe 宋体 Std R\";\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(255, 255, 215);\n"
"    \n"
"}\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    background-color: rgb(250, 250, 165);\n"
"}\n"
"QPushButton:Tooltip\n"
"{\n"
"    background-color: rgb(255,255,255)\n"
"}")
        self.calculatorBreakSeverButton.setCheckable(True)
        self.calculatorBreakSeverButton.setChecked(False)
        self.calculatorBreakSeverButton.setAutoExclusive(True)
        self.calculatorBreakSeverButton.setObjectName("calculatorBreakSeverButton")
        self.label = QtWidgets.QLabel(self.SeverBox)
        self.label.setGeometry(QtCore.QRect(0, 0, 341, 32))
        self.label.setStyleSheet("border: 1px solid #c8c8c8;\n"
"font: 10pt \"Adobe 宋体 Std R\";")
        self.label.setObjectName("label")
        self.calculatorStopSeverButton = QtWidgets.QPushButton(self.SeverBox)
        self.calculatorStopSeverButton.setEnabled(True)
        self.calculatorStopSeverButton.setGeometry(QtCore.QRect(240, 1, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std R")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.calculatorStopSeverButton.setFont(font)
        self.calculatorStopSeverButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculatorStopSeverButton.setToolTipDuration(-1)
        self.calculatorStopSeverButton.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Adobe 宋体 Std R\";\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(255, 235, 235);\n"
"    \n"
"}\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    background-color: rgb(255, 225, 225);\n"
"}\n"
"QPushButton:Tooltip\n"
"{\n"
"    background-color: rgb(255,255,255)\n"
"}")
        self.calculatorStopSeverButton.setCheckable(True)
        self.calculatorStopSeverButton.setChecked(False)
        self.calculatorStopSeverButton.setAutoExclusive(True)
        self.calculatorStopSeverButton.setObjectName("calculatorStopSeverButton")
        self.calculatorQuitSeverButton = QtWidgets.QPushButton(self.SeverBox)
        self.calculatorQuitSeverButton.setGeometry(QtCore.QRect(290, 1, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std R")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.calculatorQuitSeverButton.setFont(font)
        self.calculatorQuitSeverButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculatorQuitSeverButton.setToolTipDuration(-1)
        self.calculatorQuitSeverButton.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Adobe 宋体 Std R\";\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(255, 17, 35);\n"
"    \n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    border: 1px solid #c8c8c8;\n"
"    background-color: rgb(241, 112, 112);\n"
"}\n"
"QPushButton::checked\n"
"{\n"
"    background-color: rgb(245, 190, 190);\n"
"}\n"
"QPushButton:Tooltip\n"
"{\n"
"    background-color: rgb(255,255,255)\n"
"}")
        self.calculatorQuitSeverButton.setCheckable(True)
        self.calculatorQuitSeverButton.setChecked(False)
        self.calculatorQuitSeverButton.setAutoExclusive(True)
        self.calculatorQuitSeverButton.setObjectName("calculatorQuitSeverButton")
        self.calRunningStateLabel = QtWidgets.QLineEdit(self.SeverBox)
        self.calRunningStateLabel.setGeometry(QtCore.QRect(60, 0, 81, 32))
        self.calRunningStateLabel.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.calRunningStateLabel.setAcceptDrops(False)
        self.calRunningStateLabel.setStyleSheet("QLineEdit\n"
"{\n"
"    border: 1px solid #c8c8c8;\n"
"    border-radius:5px;\n"
"    font: 10pt \"Adobe 宋体 Std R\";\n"
"}")
        self.calRunningStateLabel.setReadOnly(True)
        self.calRunningStateLabel.setObjectName("calRunningStateLabel")
        self.label.raise_()
        self.calculatorRunSeverButton.raise_()
        self.calculatorBreakSeverButton.raise_()
        self.calculatorStopSeverButton.raise_()
        self.calculatorQuitSeverButton.raise_()
        self.calRunningStateLabel.raise_()
        self.checkUpdateButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkUpdateButton.setGeometry(QtCore.QRect(910, 690, 71, 22))
        self.checkUpdateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkUpdateButton.setToolTipDuration(-1)
        self.checkUpdateButton.setStyleSheet("QPushButton{\n"
"    font: 9pt \"Adobe 宋体 Std R\";\n"
"    border: 0px;;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(240, 245, 255);\n"
"    border: 1px solid #648cff;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border: 1px solid #646464;\n"
"    background-color: rgb(220, 230, 255);\n"
"}\n"
"QPushButton:Tooltip\n"
"{\n"
"    background-color: rgb(255,255,255)\n"
"}")
        self.checkUpdateButton.setObjectName("checkUpdateButton")
        self.calculatorBox.raise_()
        self.menu.raise_()
        self.main_title_1.raise_()
        self.main_title_2.raise_()
        self.main_title_picture.raise_()
        self.line.raise_()
        self.versionLabel.raise_()
        self.SeverBox.raise_()
        self.checkUpdateButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menuCalculatorButton.clicked.connect(self.calculatorBox.show)
        self.menuHelpButton.clicked.connect(self.calculatorBox.hide)
        self.menuAboutButton.clicked.connect(self.calculatorBox.hide)
        self.menuAboutButton_2.clicked['bool'].connect(self.calculatorBox.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "原神计算器"))
        self.menu.setTitle(_translate("MainWindow", "menu"))
        self.menuCalculatorButton.setText(_translate("MainWindow", "计算器"))
        self.menuAboutButton.setText(_translate("MainWindow", "关于"))
        self.menuHelpButton.setText(_translate("MainWindow", "帮助"))
        self.menuAboutButton_2.setText(_translate("MainWindow", "设置"))
        self.main_title_1.setText(_translate("MainWindow", "原神"))
        self.main_title_2.setText(_translate("MainWindow", "计算器"))
        self.calculatorTitle.setText(_translate("MainWindow", "计算器"))
        self.calculatorClearButton.setToolTip(_translate("MainWindow", "清空计算器输出"))
        self.calculatorClearButton.setText(_translate("MainWindow", "清空输出"))
        self.calculatorCommandLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p>在此处输入指令或内容</p></body></html>"))
        self.calculatorCommandLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">指令栏</span></p></body></html>"))
        self.calculatorCharacterInputButton.setToolTip(_translate("MainWindow", "录入角色数据"))
        self.calculatorCharacterInputButton.setText(_translate("MainWindow", "录入数据"))
        self.calculatorToolsLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p>更方便快捷的指令方式</p></body></html>"))
        self.calculatorToolsLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">常用工具</span></p></body></html>"))
        self.calculatorInjButton.setToolTip(_translate("MainWindow", "根据面板计算角色伤害"))
        self.calculatorInjButton.setText(_translate("MainWindow", "计算伤害"))
        self.calculatorHistoryButton.setToolTip(_translate("MainWindow", "查询计算并保存的伤害记录"))
        self.calculatorHistoryButton.setText(_translate("MainWindow", "查询记录"))
        self.calculatorShengYiWuInputButton.setToolTip(_translate("MainWindow", "根据圣遗物截图录入圣遗物"))
        self.calculatorShengYiWuInputButton.setText(_translate("MainWindow", "录入圣遗物"))
        self.calculatorShengYiWuCalButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>暂未支持</p></body></html>"))
        self.calculatorShengYiWuCalButton.setText(_translate("MainWindow", "计算圣遗物"))
        self.calculatorToolsmakingLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">更多工具正在制作中，联系我们:2196226582@qq.com </span></p></body></html>"))
        self.calculatorOutput.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Adobe 宋体 Std R\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.calculatorAutoClearCheckBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>指令输入后自动清空之前的输出</p></body></html>"))
        self.calculatorAutoClearCheckBox.setText(_translate("MainWindow", "自动清空"))
        self.tipsLabel.setToolTip(_translate("MainWindow", "非常实用（确信"))
        self.tipsLabel.setText(_translate("MainWindow", "Tips：向着星辰与深渊！"))
        self.versionLabel.setText(_translate("MainWindow", "version"))
        self.calculatorRunSeverButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>运行服务</p></body></html>"))
        self.calculatorRunSeverButton.setText(_translate("MainWindow", "运行"))
        self.calculatorBreakSeverButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>中断服务(立即重启)</p></body></html>"))
        self.calculatorBreakSeverButton.setText(_translate("MainWindow", "中断"))
        self.label.setText(_translate("MainWindow", " 服务"))
        self.calculatorStopSeverButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>暂停服务(手动重启)</p></body></html>"))
        self.calculatorStopSeverButton.setText(_translate("MainWindow", "暂停"))
        self.calculatorQuitSeverButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>退出</p></body></html>"))
        self.calculatorQuitSeverButton.setText(_translate("MainWindow", "退出"))
        self.calRunningStateLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">运行状态</span></p></body></html>"))
        self.calRunningStateLabel.setText(_translate("MainWindow", " 准备好了"))
        self.checkUpdateButton.setToolTip(_translate("MainWindow", "尝试检查并下载更新"))
        self.checkUpdateButton.setText(_translate("MainWindow", "检查更新"))

