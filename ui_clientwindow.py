from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from human import Human
from gameinterface import Gameinterface
import client
playerone = Human()
playertwo = Human()
game = Gameinterface()

port = 5614

class Clientwidget(QWidget):
    def __init__(self, parent=None):
        super().__init__() 
        self.c = client.Clientsocket(self)
        self.initUI()

    def __del__(self):
        self.c.stop()

    def initUI(self):
        self.setWindowTitle('클라이언트')
        # 클라이언트 설정 부분
        ipbox = QHBoxLayout()
        gb = QGroupBox('서버 설정')
        ipbox.addWidget(gb)
        box = QHBoxLayout()

        label = QLabel('Server IP')
        self.ip = QLineEdit()
        self.ip.setInputMask('000.000.000.000;_')
        box.addWidget(label)
        box.addWidget(self.ip)

        label = QLabel('Server Port')
        self.port = QLineEdit(str(port))
        box.addWidget(label)
        box.addWidget(self.port)

        self.btn = QPushButton('접속')       
        self.btn.clicked.connect(self.connectClicked)
        box.addWidget(self.btn)
        gb.setLayout(box)       

        # 채팅창 부분  
        infobox = QHBoxLayout()      
        gb = QGroupBox('Player2')        
        infobox.addWidget(gb)
        box = QVBoxLayout()

        label = QLabel('Player2 공격결과')
        box.addWidget(label)
        self.result_player2 = QTextEdit(self)
        self.result_player2.move(500, 200)
        self.result_player2.resize(340,500)
        self.result_player2.setReadOnly(True)
        box.addWidget(self.result_player2)

        hbox = QHBoxLayout()
        label = QLabel('player2 수비숫자 4자리')
        hbox.addWidget(label)
        self.player2_input_defense_num = QLineEdit(self)
        self.player2_input_defense_num.setEchoMode(QLineEdit.Password)
        self.player2_input_defense_num.move(580, 60)
        hbox.addWidget(self.player2_input_defense_num)
        
        self.btn_player2_input_defense_num = QPushButton('입력')
        self.btn_player2_input_defense_num.setAutoDefault(True)
        self.btn_player2_input_defense_num.clicked.connect(self.input_wrong_player_two_defense_num)
        self.btn_player2_input_defense_num.clicked.connect(self.input_player_two_defense_num)
        self.btn_player2_input_defense_num.clicked.connect(self.sendMsg)
        hbox.addWidget(self.btn_player2_input_defense_num)

        label = QLabel('player2 공격숫자 4자리')
        hbox.addWidget(label)
        self.player2_input_attack_num  = QLineEdit(self)
        self.player2_input_attack_num.move(580, 120)
        hbox.addWidget(self.player2_input_attack_num)
        box.addLayout(hbox)
    
        self.btn_player2_input_attack_num = QPushButton('입력')
        self.btn_player2_input_attack_num.clicked.connect(self.input_wrong_player_two_attack_num)
        self.btn_player2_input_attack_num.clicked.connect(self.input_player_two_attack_num)
        hbox.addWidget(self.btn_player2_input_attack_num)
        gb.setLayout(box)

        # 전체 배치
        vbox = QVBoxLayout()
        vbox.addLayout(ipbox)       
        vbox.addLayout(infobox)
        self.setLayout(vbox)
        self.show()


    def connectClicked(self):
        if self.c.bConnect == False:
            QMessageBox.about(self, '알림', '서버에 연결되었습니다')
            ip = self.ip.text()
            port = self.port.text()
            if self.c.connectServer(ip, int(port)):
                self.btn.setText('접속 종료')
            else:
                self.c.stop()
                self.player2_input_defense_num.clear()
                self.player2_input_attack_num .clear()
                self.btn.setText('접속')
        else:
            self.c.stop()
            self.player2_input_defense_num.clear()
            self.player2_input_attack_num .clear()
            self.btn.setText('접속')

    def updateDisconnect(self):
        self.btn.setText('접속')

    def updateMsg(self):
        pass
    
    def sendMsg(self):
        self.sendmsg = 'player2가 수비숫자를 입력하였습니다'
        self.c.send(self.sendmsg)

    def input_player_two_defense_num(self):
        self.player2_defense_num = playertwo._input_defense_num_list(self.player2_input_defense_num.text())
        print('player2 수비숫자')
        print(self.player2_defense_num)


    def input_wrong_player_two_defense_num(self):
        flag,message = playerone._input_rule_num_list(self.player2_input_defense_num.text())
        QMessageBox.about(self, '알림', message)
        self.player2_input_defense_num.setText('')
        
    def input_player_two_attack_num(self):
        player2_attack_num = playertwo._input_attack_num_list(self.player2_input_attack_num.text())
        game._strikes_and_balls_counter(playertwo,playerone,player2_attack_num)
        playertwo_strikes = playertwo.strikes
        playertwo_balls = playertwo.balls
        playertwo_trys = playertwo.trys
        self.result_player2.append(f'{playertwo_trys}차시도')
        self.result_player2.append(f'player2 공격숫자는 {player2_attack_num}입니다.')
        print(f'{self.player1_defense_num}')
        self.result_player2.append(f'결과는 {playertwo_strikes}S {playertwo_balls}B 입니다')
        self.player2_input_attack_num.setText('')
        if playertwo_strikes == 4:
            QMessageBox.about(self, '게임종료', f'    Player2가 승리하였습니다.\n\n     {playertwo_trys}번의 시도만에 맞추셨습니다.\n\nPlayer2의 수비숫자는{self.player2_defense_num}입니다.')
    
    def input_wrong_player_two_attack_num(self):
        flag,message = playertwo._input_rule_num_list(self.player2_input_attack_num.text())
        QMessageBox.about(self, '알림', message)
        self.player2_input_attack_num.setText('')
