from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
import socket, threading
# from mainwindow import Ui_MainWindow

import socket

# 접속하고자 하는 서버의 주소 및 포트
server_ip = '127.0.0.1'
server_port = 60000
address = (server_ip, server_port)

# socket을 이용해서 접속 할 준비
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect(address)  # 서버에 접속

except ConnectionRefusedError:
    print('서버 상태 / IP 주소를 확인하십시오.')
    exit()


class Ui_MainWindow(QMainWindow, object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(380, 30, 231, 192))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 10, 111, 16))
        self.label.setObjectName("label")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(380, 260, 231, 192))
        self.listView_2.setObjectName("listView_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 240, 111, 16))
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 40, 351, 261))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 31, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 10, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 330, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 360, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 390, 41, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 420, 41, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 330, 41, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 360, 41, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 390, 51, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 420, 51, 20))
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 330, 31, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 330, 31, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 360, 31, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 360, 31, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 390, 31, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 390, 31, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(80, 420, 31, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(120, 420, 31, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(260, 330, 31, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(300, 330, 31, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(260, 360, 31, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(300, 360, 31, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(260, 390, 31, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(300, 390, 31, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(260, 420, 31, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(300, 420, 31, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(80, 310, 31, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(120, 310, 31, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(260, 310, 31, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(300, 310, 31, 16))
        self.label_14.setObjectName("label_14")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 450, 75, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.btn_choice_clicked)

        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(90, 10, 271, 20))
        self.lineEdit_17.setObjectName("lineEdit_17")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 351, 251))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()

        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 349, 249))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 351, 251))
        self.label_15.setObjectName("label_15")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        pixmap = QPixmap('image/beef_increase.png') # 이미지 구현
        pixmap = pixmap.scaled(351, 251)
        self.label_15.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.lineEdit_17.setText("[5/8] 소고기 가격이 올랐습니다.")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EconomicGame"))
        self.label.setText(_translate("MainWindow", "접속한 사용자 목록"))
        self.label_2.setText(_translate("MainWindow", "Status"))
        self.pushButton.setText(_translate("MainWindow", "<"))
        self.pushButton_2.setText(_translate("MainWindow", ">"))
        self.label_3.setText(_translate("MainWindow", "커피"))
        self.label_4.setText(_translate("MainWindow", "밀가루"))
        self.label_5.setText(_translate("MainWindow", "희토류"))
        self.label_6.setText(_translate("MainWindow", "석유"))
        self.label_7.setText(_translate("MainWindow", "소고기"))
        self.label_8.setText(_translate("MainWindow", "시멘트"))
        self.label_9.setText(_translate("MainWindow", "알루미늄"))
        self.label_10.setText(_translate("MainWindow", "강철"))
        self.label_11.setText(_translate("MainWindow", "사기"))
        self.label_12.setText(_translate("MainWindow", "팔기"))
        self.label_13.setText(_translate("MainWindow", "사기"))
        self.label_14.setText(_translate("MainWindow", "팔기"))

        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.lineEdit_3.setText(_translate("MainWindow", "0"))
        self.lineEdit_4.setText(_translate("MainWindow", "0"))
        self.lineEdit_5.setText(_translate("MainWindow", "0"))
        self.lineEdit_6.setText(_translate("MainWindow", "0"))
        self.lineEdit_7.setText(_translate("MainWindow", "0"))
        self.lineEdit_8.setText(_translate("MainWindow", "0"))
        self.lineEdit_9.setText(_translate("MainWindow", "0"))
        self.lineEdit_10.setText(_translate("MainWindow", "0"))
        self.lineEdit_11.setText(_translate("MainWindow", "0"))
        self.lineEdit_12.setText(_translate("MainWindow", "0"))
        self.lineEdit_13.setText(_translate("MainWindow", "0"))
        self.lineEdit_14.setText(_translate("MainWindow", "0"))
        self.lineEdit_15.setText(_translate("MainWindow", "0"))
        self.lineEdit_16.setText(_translate("MainWindow", "0"))

        self.pushButton_3.setText(_translate("MainWindow", "결정"))

    def btn_choice_clicked(self):
        try:
            buy = int(
                self.lineEdit.text() + self.lineEdit_3.text() + self.lineEdit_5.text() + self.lineEdit_7.text() + self.lineEdit_9.text() + self.lineEdit_11.text() + self.lineEdit_13.text() + self.lineEdit_15.text())
            sale = int(
                self.lineEdit_2.text() + self.lineEdit_4.text() + self.lineEdit_6.text() + self.lineEdit_8.text() + self.lineEdit_10.text() + self.lineEdit_12.text() + self.lineEdit_14.text() + self.lineEdit_16.text())

            '''
            5개 초과 사기, 10개 초과 팔기
            음수 데이터, 정수가 아닌 데이터 입력 방지 코드
            '''

            if buy > 5:
                QMessageBox.about(self, "Economic", "5개 초과로 살 수 없습니다.")

            if sale > 10:
                QMessageBox.about(self, "Economic", "10개 초과로 팔 수 없습니다.")

            if (int(self.lineEdit.text()) < 0 or int(self.lineEdit_3.text()) < 0 or int(self.lineEdit_5.text()) < 0 or int(self.lineEdit_7.text()) < 0 or int(self.lineEdit_9.text()) < 0 or int(self.lineEdit_11.text()) < 0 or int(self.lineEdit_13.text()) < 0 or int(self.lineEdit_15.text()) < 0) \
                    or (int(self.lineEdit_2.text()) < 0 or int(self.lineEdit_4.text()) < 0 or int(self.lineEdit_6.text()) < 0 or int(self.lineEdit_8.text()) < 0 or int(self.lineEdit_10.text()) < 0 or int(self.lineEdit_12.text()) < 0 or int(self.lineEdit_14.text()) < 0 or int(self.lineEdit_16.text()) < 0):
                QMessageBox.about(self, "Economic", "0~10 범위 내로 값을 올바르게 입력하였는지 다시 확인해 주시기 바랍니다.")


        except ValueError:
            QMessageBox.about(self, "Economic", "0~10 범위 내로 값을 올바르게 입력하였는지 다시 확인해 주시기 바랍니다.")

        # else:
            # Dict 만들어 주고 서버로 전송하는 부분 추가


        # print(self.lineEdit.text())
        # print(self.lineEdit_3.text())
        # print(self.lineEdit_5.text())
        # print(self.lineEdit_7.text())
        # print(self.lineEdit_9.text())
        # print(self.lineEdit_11.text())
        # print(self.lineEdit_13.text())
        # print(self.lineEdit_15.text())


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setMinimumSize(QSize(620, 506))
        self.setWindowTitle("Economic")

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
