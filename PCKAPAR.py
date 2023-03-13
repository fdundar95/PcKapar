# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,QDateTime,QTime
import datetime
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.count = 0
        self.start = False
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(148, 203)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(0, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName("timeEdit")
        
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(0, 10, 91, 16))
        self.info.setObjectName("info")
        
        self.screen = QtWidgets.QLabel(self.centralwidget)
        self.screen.setGeometry(QtCore.QRect(10, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.screen.setFont(font)
        self.screen.setFrameShape(QtWidgets.QFrame.Box)
        self.screen.setFrameShadow(QtWidgets.QFrame.Plain)
        self.screen.setObjectName("screen")
        
        self.info_2 = QtWidgets.QLabel(self.centralwidget)
        self.info_2.setGeometry(QtCore.QRect(0, 110, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.info_2.setFont(font)
        self.info_2.setObjectName("info_2")
        
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(30, 70, 81, 31))
        self.start_button.setObjectName("start_button")
        
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(30, 170, 81, 31))
        self.reset_button.setObjectName("reset_button")
        
        self.set_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_button.setGeometry(QtCore.QRect(110, 30, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.set_button.setFont(font)
        self.set_button.setObjectName("pushButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000) 

        self.start_button.clicked.connect(self.start_action)
        self.set_button.clicked.connect(self.set_time)
        self.reset_button.clicked.connect(self.reset_action)
     
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def start_action(self):
        self.start = True
        if self.count == 0:
            self.start = False
        self.start_button.setEnabled(False)
        self.reset_button.setEnabled(True)
  
    def set_time(self):
        self.start = False
        t = self.timeEdit.time()
        self.count = ((t.hour()) * 3600) + ((t.minute()) * 60) + ((t.second()))
        self.screen.setText((str(t.hour())) + ":" + (str(t.minute())) + ":" + (str(t.second())))

    def showTime(self):
        if self.start:
            self.count -= 1
            if self.count == 0: 
                self.start = False
                self.screen.setText("Elveda...")
                os.system("shutdown /s /t 1")
        
        if self.start: 
            hmsformat = str(datetime.timedelta(seconds=self.count))
            self.screen.setText(hmsformat)
            
    def reset_action(self):
        self.start = False
        self.count = 0
        self.screen.setText("00:00:00")
        self.start_button.setEnabled(True)
        self.reset_button.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PCKAPAR"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.info.setText(_translate("MainWindow", "saat:dakika:saniye"))
        self.screen.setText(_translate("MainWindow", "00:00:00"))
        self.info_2.setText(_translate("MainWindow", "Kapanmaya kalan süre:"))
        self.start_button.setText(_translate("MainWindow", "BAŞLAT"))
        self.set_button.setText(_translate("MainWindow", "ONAY"))
        self.reset_button.setText(_translate("MainWindow", "RESETLE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())