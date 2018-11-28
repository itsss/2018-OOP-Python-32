# # pythonspot.com
#
# import sys
# from PyQt5.QtGui import QIcon, QPixmap
# from PyQt5 import QtCore, QtWidgets
# from PyQt5.QtWidgets import *
#
# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.title = 'OOP_Economic'
#         self.left = 10
#         self.top = 10
#         self.width = 640
#         self.height = 480
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         # Create widget
#         label = QLabel(self)
#         pixmap = QPixmap('image/beef_increase.png')
#         pixmap.scaled(32, 32, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#         label.setPixmap(pixmap)
#
#         self.resize(pixmap.width(), pixmap.height())
#         self.title = QLabel("소고기 가격이 올랐습니다", self)
#         self.title.setStyleSheet("font: 30pt; color:black")
#         self.title.setAlignment(QtCore.Qt.AlignBottom)
#
#         btn1 = QPushButton("<", self)
#         btn1.move(20, 20)
#         btn1.clicked.connect(self.btn1_clicked)
#
#         btn2 = QPushButton(">", self)
#         btn2.move(80, 20)
#         btn2.clicked.connect(self.btn2_clicked)
#
#         self.show()
#
#     def btn1_clicked(self):
#         QMessageBox.about(self, "message", "이전 그림 보기")
#
#     def btn2_clicked(self):
#         QMessageBox.about(self, "message", "다음 그림 보기")
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import QSize
import socket, threading
# from mainwindow import Ui_MainWindow
# Ref: https://stackoverflow.com/questions/11812000/login-dialog-pyqt

class Connect(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Connect, self).__init__(parent)
        self.serverIP = QtWidgets.QLineEdit(self)
        self.buttonconn = QtWidgets.QPushButton('Connect', self)
        self.buttonconn.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.serverIP)
        layout.addWidget(self.buttonconn)

    def handleLogin(self):
        var = self.serverIP.text()
        serv = (str(var), 50000)
        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sck.settimeout(5)
            sck.connect(serv)
            self.accept()

        except ConnectionRefusedError:
            QMessageBox.about(self, "Economic", "서버 상태를 확인하십시오.")
        except OSError:
            QMessageBox.about(self, "Economic", "서버 상태를 확인하십시오.")

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("Economic")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    conn = Connect()

    if conn.exec_() == QtWidgets.QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())
