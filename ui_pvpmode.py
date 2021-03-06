import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtCore
from human import Human
from gameinterface import Gameinterface
playerone = Human() 
playertwo = Human()
game = Gameinterface()
class Pvpmode(QWidget):
    def __init__(self, parent=None):
        super(Pvpmode, self).__init__()
        self.setWindowTitle('Bulls and Cows')
        self.setGeometry(400, 100, 900, 800)
        self.addInput()
        self.addButtons()
        self.addResult()
        
    def addInput(self):
        self.player1_input_defense_num_title = QLabel("Player1의 수비숫자",self)
        self.player1_input_defense_num_title.move(130,40)
        self.player1_input_defense_num = QLineEdit(self)
        self.player1_input_defense_num.setEchoMode(QLineEdit.Password)
        self.player1_input_defense_num.move(130, 60)
        self.player1_input_attack_num_title = QLabel("Player1의 공격숫자 4자리  ", self)
        self.player1_input_attack_num_title.move(130,100)
        self.player1_input_attack_num = QLineEdit(self)
        self.player1_input_attack_num.move(130, 120)
        self.player2_input_defense_num_title = QLabel("Player2의 수비숫자",self)
        self.player2_input_defense_num_title.move(580,40)
        self.player2_input_defense_num = QLineEdit(self)
        self.player2_input_defense_num.setEchoMode(QLineEdit.Password)
        self.player2_input_defense_num.move(580, 60)
        self.player2_input_attack_num_title = QLabel("Player2의 공격숫자 4자리 ", self)
        self.player2_input_attack_num_title.move(580,100)
        self.player2_input_attack_num  = QLineEdit(self)
        self.player2_input_attack_num.move(580, 120)

    def addButtons(self):
        self.btn_player1_input_defense_num  = QPushButton(self)
        self.btn_player1_input_defense_num.setText('입력')
        self.btn_player1_input_defense_num.clicked.connect(self.input_wrong_player_one_defense_num)
        self.btn_player1_input_defense_num.clicked.connect(self.input_player_one_defense_num)
        self.btn_player1_input_defense_num.resize(80, 33)
        self.btn_player1_input_defense_num.move(250, 60)
        self.btn_player1_input_attack_num = QPushButton(self)
        self.btn_player1_input_attack_num.setText('입력')
        self.btn_player1_input_attack_num.resize(80, 33)
        self.btn_player1_input_attack_num.move(250, 120)
        self.btn_player1_input_attack_num.clicked.connect(self.input_wrong_player_one_attack_num)
        self.btn_player1_input_attack_num.clicked.connect(self.input_player_one_attack_num)
        self.btn_player2_input_defense_num = QPushButton(self)
        self.btn_player2_input_defense_num.setText('입력')
        self.btn_player2_input_defense_num.clicked.connect(self.input_wrong_player_two_defense_num)
        self.btn_player2_input_defense_num.clicked.connect(self.input_player_two_defense_num)
        self.btn_player2_input_defense_num.resize(80, 33)
        self.btn_player2_input_defense_num.move(700, 60)
        self.btn_player2_input_attack_num = QPushButton(self)
        self.btn_player2_input_attack_num.setText('입력')
        self.btn_player2_input_attack_num.resize(80, 33)
        self.btn_player2_input_attack_num.move(700, 120)
        self.btn_player2_input_attack_num.clicked.connect(self.input_wrong_player_two_attack_num)
        self.btn_player2_input_attack_num.clicked.connect(self.input_player_two_attack_num)

    def addResult(self):
        self.result_player1 = QTextEdit(self)
        self.result_player1.move(80, 200)
        self.result_player1.resize(340,500)
        self.result_player1.setReadOnly(True)
        self.result_player2 = QTextEdit(self)
        self.result_player2.move(500, 200)
        self.result_player2.resize(340,500)
        self.result_player2.setReadOnly(True)

    def input_player_one_defense_num(self):
        self.player1_defense_num = playerone._input_defense_num_list(self.player1_input_defense_num.text())
        print('player1 수비숫자')
        print(self.player1_defense_num)
        
    
    def input_player_two_defense_num(self):
        self.player2_defense_num = playertwo._input_defense_num_list(self.player2_input_defense_num.text())
        print('player2 수비숫자')
        print(self.player2_defense_num)

        
    
    def input_wrong_player_one_defense_num(self):
        flag,message = playerone._input_rule_num_list(self.player1_input_defense_num.text())
        QMessageBox.about(self, '알림', message)
        self.player1_input_defense_num.setText('')
    
    def input_wrong_player_two_defense_num(self):
        flag,message = playerone._input_rule_num_list(self.player2_input_defense_num.text())
        QMessageBox.about(self, '알림', message)
        self.player2_input_defense_num.setText('')
        

    
    def input_player_one_attack_num(self):
        player1_attack_num = playerone._input_attack_num_list(self.player1_input_attack_num.text())
        game._strikes_and_balls_counter(playerone,playertwo,player1_attack_num)
        playerone_strikes = playerone.strikes
        playerone_balls = playerone.balls
        playerone_trys = playerone.trys
        self.result_player1.append(f'{playerone_trys}차시도')
        self.result_player1.append(f'player1 공격숫자는 {player1_attack_num}입니다.')
        self.result_player1.append(f'결과는 {playerone_strikes}S {playerone_balls}B 입니다')
        self.player1_input_attack_num.setText('')
        if playerone_strikes == 4:
            QMessageBox.about(self, '게임종료', f'    Player1이 승리하였습니다.\n\n     {playerone_trys}번의 시도만에 맞추셨습니다.\n\nPlayer1의 수비숫자는{self.player1_defense_num}입니다.')

    def input_player_two_attack_num(self):
        player2_attack_num = playertwo._input_attack_num_list(self.player2_input_attack_num.text())
        game._strikes_and_balls_counter(playertwo,playerone,player2_attack_num)
        playertwo_strikes = playertwo.strikes
        playertwo_balls = playertwo.balls
        playertwo_trys = playertwo.trys
        self.result_player2.append(f'{playertwo_trys}차시도')
        self.result_player2.append(f'player2 공격숫자는 {player2_attack_num}입니다.')
        self.result_player2.append(f'결과는 {playertwo_strikes}S {playertwo_balls}B 입니다')
        self.player2_input_attack_num.setText('')
        if playertwo_strikes == 4:
            QMessageBox.about(self, '게임종료', f'    Player2가 승리하였습니다.\n\n     {playertwo_trys}번의 시도만에 맞추셨습니다.\n\nPlayer2의 수비숫자는{self.player2_defense_num}입니다.')

        

    def input_wrong_player_one_attack_num(self):
        flag,message = playerone._input_rule_num_list(self.player1_input_attack_num.text())
        QMessageBox.about(self, '알림', message)
        self.player1_input_attack_num.setText('')
    
    def input_wrong_player_two_attack_num(self):
        flag,message = playertwo._input_rule_num_list(self.player2_input_attack_num.text())
        QMessageBox.about(self, '알림', message)
        self.player2_input_attack_num.setText('')