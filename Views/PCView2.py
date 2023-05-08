# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PCView2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from tkinter import filedialog
from datetime import datetime
import time, os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, master):
        MainWindow.setObjectName("MainWindow")
        self.master= master
        self.MainWindow= MainWindow
        MainWindow.setWindowIcon(QtGui.QIcon(os.getcwd() + "/CompassX.ico"))
        MainWindow.setEnabled(True)
        MainWindow.resize(686, 532)
        MainWindow.setMaximumSize(QtCore.QSize(686, 532))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setWindowTitle("Compass X - Protocolo Compass3D 2023 Edition")
        MainWindow.setWindowOpacity(21.0)
        MainWindow.setStyleSheet("\n"
"background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.00568182 rgba(255, 129, 0, 255), stop:1 rgba(255, 91, 0, 255))")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 281, 91))
        font = QtGui.QFont()
        font.setFamily("Sora bold")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"background: transparent;\n"
"font-weight: bold;\n"
"font: 26pt \"Sora bold\";")
        self.label.setObjectName("label")
        self.ANP = QtWidgets.QSlider(self.centralwidget)
        self.ANP.setGeometry(QtCore.QRect(550, 190, 101, 41))
        self.ANP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ANP.setStyleSheet("QSlider::handle:horizontal{\n"
"    background: #ff8100;\n"
"    border: 1px solid black;\n"
"}\n"
"QSlider:horizontal{\n"
"    background: transparent;\n"
"    border: 1px solid black;\n"
"}\n"
"QSlider::add-page{\n"
"    border:1px solid black;\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page{\n"
"    border:1px solid black;\n"
"    background:  #ff9c38;\n"
"}")
        self.ANP.setMaximum(1)
        self.ANP.setOrientation(QtCore.Qt.Horizontal)
        self.ANP.setObjectName("ANP")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 180, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Sora")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: transparent;\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(435, 247, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Sora")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: transparent;\n"
"color: white;")
        self.label_3.setObjectName("label_3")
        self.POGNP = QtWidgets.QSlider(self.centralwidget)
        self.POGNP.setGeometry(QtCore.QRect(550, 250, 101, 41))
        self.POGNP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.POGNP.setStyleSheet("QSlider::handle:horizontal{\n"
"    background: #ff8100;\n"
"    border: 1px solid black;\n"
"}\n"
"QSlider:horizontal{\n"
"    background: transparent;\n"
"    border: 1px solid black;\n"
"}\n"
"QSlider::add-page{\n"
"    border:1px solid black;\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page{\n"
"    border:1px solid black;\n"
"    background:  #ff9c38;\n"
"}")
        self.POGNP.setMaximum(1)
        self.POGNP.setOrientation(QtCore.Qt.Horizontal)
        self.POGNP.setObjectName("POGNP")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(433, 309, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Sora")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background: transparent;\n"
"color: white;")
        self.label_4.setObjectName("label_4")
        self.GNMSP = QtWidgets.QSlider(self.centralwidget)
        self.GNMSP.setGeometry(QtCore.QRect(550, 310, 101, 41))
        self.GNMSP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GNMSP.setStyleSheet("QSlider::handle:horizontal{\n"
"    background: #ff8100;\n"
"    border: 1px solid black;\n"
"}\n"
"QSlider:horizontal{\n"
"    background: transparent;\n"
"    border: 1px solid black;\n"
"}\n"
"QSlider::add-page{\n"
"    border:1px solid black;\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page{\n"
"    border:1px solid black;\n"
"    background:  #ff9c38;\n"
"}")
        self.GNMSP.setMaximum(1)
        self.GNMSP.setOrientation(QtCore.Qt.Horizontal)
        self.GNMSP.setObjectName("GNMSP")
        self.LDM = QtWidgets.QSlider(self.centralwidget)
        self.LDM.setGeometry(QtCore.QRect(550, 370, 101, 41))
        self.LDM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LDM.setStyleSheet("QSlider::handle:horizontal{\n"
"    background: #ff8100;\n"
"    border: 1px solid black;\n"
"}\n"
"QSlider:horizontal{\n"
"    background: transparent;\n"
"    border: 1px solid black;\n"
"}\n"
"QSlider::add-page{\n"
"    border:1px solid black;\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page{\n"
"    border:1px solid black;\n"
"    background:  #ff9c38;\n"
"}")
        self.LDM.setMaximum(1)
        self.LDM.setOrientation(QtCore.Qt.Horizontal)
        self.LDM.setObjectName("LDM")
        self.UDM = QtWidgets.QSlider(self.centralwidget)
        self.UDM.setGeometry(QtCore.QRect(550, 430, 101, 41))
        self.UDM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.UDM.setStyleSheet("QSlider::handle:horizontal{\n"
"    background: #ff8100;\n"
"    border: 1px solid black;\n"
"}\n"
"QSlider:horizontal{\n"
"    background: transparent;\n"
"    border: 1px solid black;\n"
"}\n"
"QSlider::add-page{\n"
"    border:1px solid black;\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page{\n"
"    border:1px solid black;\n"
"    background:  #ff9c38;\n"
"}")
        self.UDM.setMaximum(1)
        self.UDM.setOrientation(QtCore.Qt.Horizontal)
        self.UDM.setObjectName("UDM")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(478, 368, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Sora")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background: transparent;\n"
"color: white;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(474, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Sora")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background: transparent;\n"
"color: white;")
        self.label_6.setObjectName("label_6")
        self.DENTICAO = QtWidgets.QComboBox(self.centralwidget)
        self.DENTICAO.setGeometry(QtCore.QRect(40, 120, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Sora")
        font.setPointSize(14)
        self.DENTICAO.setFont(font)
        self.DENTICAO.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DENTICAO.setStyleSheet("QComboBox{\n"
"    background: transparent;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QComboBox:selected{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"    background: white;\n"
"}\n"
"")
        self.DENTICAO.setObjectName("DENTICAO")
        self.DENTICAO.addItem("")
        self.DENTICAO.addItem("")
        self.DENTICAO.addItem("")
        self.NASCIMENTO = QtWidgets.QDateEdit(self.centralwidget)
        self.NASCIMENTO.setGeometry(QtCore.QRect(40, 230, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NASCIMENTO.sizePolicy().hasHeightForWidth())
        self.NASCIMENTO.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sora")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.NASCIMENTO.setFont(font)
        self.NASCIMENTO.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NASCIMENTO.setStyleSheet("QDateEdit{\n"
"    background: white;\n"
"    justify-content: center;\n"
"}\n"
"\n"
"QDateEdit QWidget{\n"
"    background: white;\n"
"    color: black;\n"
"}")
        self.NASCIMENTO.setCalendarPopup(True)
        self.NASCIMENTO.setObjectName("NASCIMENTO")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 280, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Sora")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background: transparent;\n"
"color: white;")
        self.label_8.setObjectName("label_8")
        self.TOMOGRAFIA = QtWidgets.QDateEdit(self.centralwidget)
        self.TOMOGRAFIA.setGeometry(QtCore.QRect(40, 330, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TOMOGRAFIA.sizePolicy().hasHeightForWidth())
        self.TOMOGRAFIA.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sora")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.TOMOGRAFIA.setFont(font)
        self.TOMOGRAFIA.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TOMOGRAFIA.setStyleSheet("QDateEdit{\n"
"    background: white;\n"
"    justify-content: center;\n"
"}\n"
"\n"
"QDateEdit QWidget{\n"
"    background: white;\n"
"    color: black;\n"
"}")
        self.TOMOGRAFIA.setCalendarPopup(True)
        self.TOMOGRAFIA.setObjectName("TOMOGRAFIA")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(460, 190, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Sora")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background: transparent;\n"
"color: white;")
        self.label_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_9.setObjectName("label_9")
        self.TXTFILE = QtWidgets.QLabel(self.centralwidget)
        self.TXTFILE.setGeometry(QtCore.QRect(30, 410, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Sora")
        font.setPointSize(16)
        self.TXTFILE.setFont(font)
        self.TXTFILE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TXTFILE.setStyleSheet("background: transparent;\n"
"color: white;")
        self.TXTFILE.setAlignment(QtCore.Qt.AlignCenter)
        self.TXTFILE.setObjectName("TXTFILE")
        self.BTNFILE = QtWidgets.QPushButton(self.centralwidget)
        self.BTNFILE.setGeometry(QtCore.QRect(40, 400, 301, 61))
        self.BTNFILE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BTNFILE.setStyleSheet("background: transparent; border: 1px solid white")
        self.BTNFILE.setText("")
        self.BTNFILE.setObjectName("BTNFILE")
        self.BTNFILE.clicked.connect(self.openFileNamesDialog)
        self.TXTFILE.raise_()
        self.BTNFILE.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def openFileNamesDialog(self):
        print("To aqui")
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self.MainWindow,"Selecione o arquivo CSV", "","CSV Files(*.csv)", options=options)
        last= files[0].split("/")[len(files[0].split("/"))-1]
        if(".csv" in last):        
            self.TXTFILE.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">{last}</span></p></body></html>")
            self.FILESELECT= files[0]
            self.handShake()
        else:
            self.TXTFILE.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">Formato Inválido</span></p></body></html>")
            self.FILESELECT= None
    def handShake(self):
        self.master.forms= {
            "A - Np": self.ANP.value(),
            "Pog - Np": self.POGNP.value(),
            "Gn MSP": self.GNMSP.value(),
            "LDM": self.LDM.value(),
            "UDM": self.UDM.value()
        }
        self.master.filepath= self.FILESELECT
        self.master.denticao= self.DENTICAO.currentText()
        datanascimento= self.NASCIMENTO.date()
        dataatual= self.TOMOGRAFIA.date()
        if(dataatual.month() < datanascimento.month()):
            self.master.idade= dataatual.year() - datanascimento.year() - 1
        elif(dataatual.month() == datanascimento.month() and datanascimento.day() < dataatual.day()):
            self.master.idade= dataatual.year() - datanascimento.year() - 1
        else:
            self.master.idade= dataatual.year() - datanascimento.year()
        self.MainWindow.close()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "CompassX"))
        self.label_2.setText(_translate("MainWindow", "Data de Nascimento"))
        self.label_3.setText(_translate("MainWindow", "Pog - Np"))
        self.label_4.setText(_translate("MainWindow", "Gn - MSP"))
        self.label_5.setText(_translate("MainWindow", "LDM"))
        self.label_6.setText(_translate("MainWindow", "UDM"))
        self.DENTICAO.setItemText(0, _translate("MainWindow", "Decídua"))
        self.DENTICAO.setItemText(1, _translate("MainWindow", "Mista"))
        self.DENTICAO.setItemText(2, _translate("MainWindow", "Permanente"))
        self.label_8.setText(_translate("MainWindow", "Data da Tomografia"))
        self.label_9.setText(_translate("MainWindow", "A - Np"))
        self.TXTFILE.setText(_translate("MainWindow", "Selecione o arquivo CSV"))

class Execute:
    def __init__(self):
        app = QtWidgets.QApplication([])
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow, self)
        MainWindow.show()
        app.exec_()