import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtCore
from ui_pvemode import Pvemode
from ui_selectsocket import Selectsocket
class Gamemodeselector(QWidget):
    def __init__(self):
        super(Gamemodeselector, self).__init__()
        self.setWindowTitle('Bulls and Cows')
        self.setGeometry(400, 100, 900, 800)
        self.addTitle()
        self.addButtons()

    def addTitle(self):
        self.label = QLabel('숫자야구', self)
        self.label.resize(900, 100)
        self.label.setAlignment(Qt.AlignCenter)
        #글자 크기 변경 
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label.setFont(font)

    def addButtons(self):
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_pvemode = QPushButton(self)
        self.btn_pvemode.setText('PVE모드')
        self.btn_pvemode.resize(340, 500)
        self.btn_pvemode.move(80, 200)
        self.btn_pvemode.setFont(font)
        self.btn_pvemode.clicked.connect(self.selectpvemode)
        self.btn_pvpmode = QPushButton(self)
        self.btn_pvpmode.setText('PVP모드')
        self.btn_pvpmode.resize(340, 500)
        self.btn_pvpmode.move(500, 200)
        self.btn_pvpmode.setFont(font)
        self.btn_pvpmode.clicked.connect(self.select_client_and_server)
        self.pvemode =Pvemode(self)
        self.selector = Selectsocket(self)


    def selectpvemode(self):
        self.pvemode.show()

    def select_client_and_server(self):
        self.selector.show()
    
        

