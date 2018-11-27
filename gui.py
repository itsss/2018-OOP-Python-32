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
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QLineEdit
from PyQt5.QtCore import QSize

# Ref: https://pythonprogramminglanguage.com/pyqt5-hello-world/
class HelloWindow(QMainWindow):
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )

