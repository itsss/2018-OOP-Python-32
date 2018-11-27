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

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import QSize
import socket, threading

class intro(QMainWindow):
    '''
    프로그램을 작동할 때 클라이언트에서 뜨는 화면입니다.
    '''
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(250, 140))
        self.setWindowTitle("Economic")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        self.ui()

    def ui(self):
        btn = QPushButton('connect', self)
        btn.setToolTip('start game')
        btn.move(50, 50)

        btn2 = QPushButton('quit', self)
        btn2.setToolTip('quit game')
        btn2.move(50, 80)

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('서버주소:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(100, 25)
        self.nameLabel.move(20, 20)

        btn.clicked.connect(self.push1)
        # btn2.clicked.connect(exit())

    def push1(self):
        '''
        사용자가 connect 버튼을 눌렀을 때 사용하는 함수
        :return:
        '''
        var = self.line.text()
        print(var)
        ip = str(var)
        port = 50035
        serv = (ip, port)

        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('234234')
        # ip = '127.0.0.1'
        # print(type(ip))

        # 접속하는 부분(코드 118번) 에서 응답 없음 오류 발생
        # 해결 방안이 필요
        try:
            sck.connect(serv)
        except ConnectionRefusedError:
            QMessageBox.about(self, "Economic", "서버 상태를 확인하십시오.")
            print('서버 상태를 확인하십시오.')

        except OSError:
            print('서버 IP를 올바르게 입력하세요.')
            QMessageBox.about(self, "Economic", "서버 IP를 올바르게 입력하세요.")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = intro()
    mainWin.show()
    sys.exit( app.exec_() )

