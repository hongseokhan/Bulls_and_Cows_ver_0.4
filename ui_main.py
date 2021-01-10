from ui_selectgamemode import Gamemodeselector
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtCore

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Gamemodeselector()
    game.show()
    sys.exit(app.exec_())