# pythonspot.com

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *



class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'OOP_Economic'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('image/beef_increase.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.title = QLabel("소고기 가격이 올랐습니다", self)
        self.title.setStyleSheet("font: 30pt; color:black")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())