# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!


import sys
import time
from pypresence import Presence
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    id = ''
    details = ''
    state = ''
    image = ''
    timer = 0
    RPC = None
    discord_status = False
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(10, 40, 241, 20))
        self.label_id.setObjectName("label_id")
        self.label_details = QtWidgets.QLabel(self.centralwidget)
        self.label_details.setGeometry(QtCore.QRect(10, 140, 241, 20))
        self.label_details.setObjectName("label_details")
        self.label_state = QtWidgets.QLabel(self.centralwidget)
        self.label_state.setGeometry(QtCore.QRect(10, 210, 241, 20))
        self.label_state.setObjectName("label_state")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(10, 280, 241, 20))
        self.label_image.setObjectName("label_image")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 160, 121, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 230, 121, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 300, 121, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(300, 60, 121, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(10, 60, 241, 20))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_details = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_details.setGeometry(QtCore.QRect(10, 160, 241, 20))
        self.lineEdit_details.setObjectName("lineEdit_details")
        self.lineEdit_state = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_state.setGeometry(QtCore.QRect(10, 230, 241, 20))
        self.lineEdit_state.setObjectName("lineEdit_state")
        self.lineEdit_image = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_image.setGeometry(QtCore.QRect(10, 300, 241, 20))
        self.lineEdit_image.setObjectName("lineEdit_image")
        self.checkBox_timer = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_timer.setGeometry(QtCore.QRect(280, 60, 16, 16))
        self.checkBox_timer.setText("")
        self.checkBox_timer.setObjectName("checkBox_timer")
        self.checkBox_details = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_details.setGeometry(QtCore.QRect(280, 160, 16, 16))
        self.checkBox_details.setText("")
        self.checkBox_details.setObjectName("checkBox_details")
        self.checkBox_state = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_state.setGeometry(QtCore.QRect(280, 230, 16, 16))
        self.checkBox_state.setText("")
        self.checkBox_state.setObjectName("checkBox_state")
        self.checkBox_image = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_image.setGeometry(QtCore.QRect(280, 300, 16, 16))
        self.checkBox_image.setText("")
        self.checkBox_image.setObjectName("checkBox_image")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(10, 360, 241, 31))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(10, 420, 241, 31))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_hide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hide.setGeometry(QtCore.QRect(10, 480, 241, 31))
        self.pushButton_hide.setObjectName("pushButton_hide")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.uptate_data()
        MainWindow.setWindowTitle(_translate("Discord Rich Presence", "Discord Rich Presence"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Show details</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Show state</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Show image</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Show timer</span></p></body></html>"))
        self.pushButton_save.setText(_translate("MainWindow", "Save Change"))
        self.pushButton_start.setText(_translate("MainWindow", "Start RPC"))
        self.pushButton_hide.setText(_translate("MainWindow", "Hide Window"))

    def uptate_data(self):
        with open('data.txt', 'r', encoding = 'utf-8') as f:
            self.id = f.readline().strip()
            self.details = f.readline().strip()
            self.state = f.readline().strip()
            self.image = f.readline().strip()

        _translate = QtCore.QCoreApplication.translate
        self.label_id.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Client ID : %s</span></p></body></html>" % self.id))
        self.label_details.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Details : %s</span></p></body></html>" % self.details))
        self.label_state.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : %s</span></p></body></html>" % self.state))
        self.label_image.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Image : %s</span></p></body></html>" % self.image))

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.pushButton_start.clicked.connect(self.start)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_hide.clicked.connect(self.hide_window)

    def start(self):
        _translate = QtCore.QCoreApplication.translate
        if self.discord_status == False:
            self.pushButton_start.setText(_translate("MainWindow", "Stop RPC"))
            self.uptate_data()
            if self.checkBox_timer.isChecked() == False:
                self.timer = None
            else:
                self.timer = int(time.time())
            if self.checkBox_details.isChecked() == False:
                self.details = None
            if self.checkBox_state.isChecked() == False:
                self.state = None
            if self.checkBox_image.isChecked() == False:
                self.image = None
            self.RPC = Presence(client_id = self.id)
            self.RPC.connect()
            self.RPC.update(large_image = self.image, details = self.details, state = self.state, start = self.timer)
            self.discord_status = True
        else:
            self.discord_status = False
            self.RPC.clear()
            self.RPC.close()
            self.pushButton_start.setText(_translate("MainWindow", "Start RPC"))

    def save(self):
        with open('data.txt', 'w+', encoding = 'utf-8') as f:
            if len(self.lineEdit_id.text()) > 0: f.write(self.lineEdit_id.text() + '\n')
            else: f.write(self.id + '\n')
            if len(self.lineEdit_details.text()) > 0: f.write(self.lineEdit_details.text() + '\n')
            else: f.write(self.details + '\n')
            if len(self.lineEdit_state.text()) > 0: f.write(self.lineEdit_state.text() + '\n')
            else: f.write(self.state + '\n')
            if len(self.lineEdit_image.text()) > 0: f.write(self.lineEdit_image.text() + '\n')
            else: f.write(self.image + '\n')
        self.uptate_data()

    def hide_window(self):
        self.hide()
        self.mSysTrayIcon = QtWidgets.QSystemTrayIcon(self)
        icon = QtGui.QIcon("icon.png")
        self.mSysTrayIcon.setIcon(icon)
        self.mSysTrayIcon.setToolTip("Discord Rich Presence")
        self.mSysTrayIcon.activated.connect(self.on_activated)
        self.mSysTrayIcon.show()

    def on_activated(self, reason):
        if reason == self.mSysTrayIcon.Trigger:
            self.show()
            self.mSysTrayIcon.hide()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
