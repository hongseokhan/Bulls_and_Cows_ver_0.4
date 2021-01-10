from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from ui_serverwindow import Serverwidget
from ui_clientwindow import Clientwidget

class Selectsocket(QDialog):
    def __init__(self,parent=None):
        super().__init__()
        # 윈도우 설정
        self.setGeometry(300, 300, 400, 200)  # x, y, w, h
        self.setWindowTitle('Server and Clinet')
        # QButton 위젯 생성
        self.server_button = QPushButton('Server', self)
        self.server_button.clicked.connect(self.selectclientwidget)
        self.server_button.setGeometry(10, 10, 180, 150)
        self.client_button = QPushButton('Client', self)
        self.client_button.clicked.connect(self.selectserverwidget)
        self.client_button.setGeometry(210, 10, 180, 150)

    def selectclientwidget(self):
        self.server = Serverwidget(self)
    def selectserverwidget(self):
        self.client = Clientwidget(self)
