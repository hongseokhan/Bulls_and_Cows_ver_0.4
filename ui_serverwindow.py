from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import socket
import server
from human import Human
from gameinterface import Gameinterface
playerone = Human()
playertwo = Human() 
game = Gameinterface()
port = 5614

class Serverwidget(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.s = server.Serversocket(self)
        self.initUI()

    def initUI(self):
        #서버 설정(IP,Port 입력)
        self.setWindowTitle('서버')
        ipbox = QHBoxLayout()
        server_setting = QGroupBox('서버 설정')
        ipbox.addWidget(server_setting)
        ip_port_input_box = QHBoxLayout()
        label = QLabel('Server IP')
        self.ip = QLineEdit(socket.gethostbyname(socket.gethostname()))
        ip_port_input_box.addWidget(label)
        ip_port_input_box.addWidget(self.ip)
        label = QLabel('Server Port')
        self.port = QLineEdit(str(port))
        ip_port_input_box.addWidget(label)
        ip_port_input_box.addWidget(self.port)
        self.btn = QPushButton('서버 실행')
        self.btn.setCheckable(True)        
        self.btn.toggled.connect(self.toggleButton)
        ip_port_input_box.addWidget(self.btn)
        server_setting.setLayout(ip_port_input_box)

        # 접속자 정보 부분
        infobox = QHBoxLayout()
        gb = QGroupBox('접속자 정보')
        infobox.addWidget(gb)
        box = QVBoxLayout()        

        self.guest = QTableWidget()
        self.guest.setRowCount(1)
        self.guest.setColumnCount(2)      
        self.guest.setHorizontalHeaderItem(0, QTableWidgetItem('ip'))
        self.guest.setHorizontalHeaderItem(1, QTableWidgetItem('port'))                
        box.addWidget(self.guest)
        gb.setLayout(box)


        gb = QGroupBox('Player1')        
        infobox.addWidget(gb)
        box = QVBoxLayout()
        label = QLabel('Player1 공격결과')
        box.addWidget(label)
        self.result_player1 = QTextEdit(self)
        self.result_player1.move(500, 200)
        self.result_player1.resize(340,500)
        self.result_player1.setReadOnly(True)
        box.addWidget(self.result_player1)
        hbox = QHBoxLayout()

        label = QLabel('player1 수비숫자 4자리')
        hbox.addWidget(label)
        self.player1_input_defense_num = QLineEdit(self)
        self.player1_input_defense_num.setEchoMode(QLineEdit.Password)
        self.player1_input_defense_num.move(580, 60)
        hbox.addWidget(self.player1_input_defense_num)
        self.btn_player1_input_defense_num = QPushButton('입력')
        self.btn_player1_input_defense_num.setAutoDefault(True)
        self.btn_player1_input_defense_num.clicked.connect(self.input_wrong_player_one_defense_num)
        self.btn_player1_input_defense_num.clicked.connect(self.input_player_one_defense_num)
        self.btn_player1_input_defense_num.clicked.connect(self.sendMsg)
        hbox.addWidget(self.btn_player1_input_defense_num)

        label = QLabel('player1 공격숫자 4자리')
        hbox.addWidget(label)
        self.player1_input_attack_num  = QLineEdit(self)
        self.player1_input_attack_num.move(580, 120)
        hbox.addWidget(self.player1_input_attack_num)
        box.addLayout(hbox)
    
        self.btn_player1_input_attack_num = QPushButton('입력')
        self.btn_player1_input_attack_num.clicked.connect(self.input_wrong_player_one_attack_num)
        self.btn_player1_input_attack_num.clicked.connect(self.input_player_one_attack_num)
        hbox.addWidget(self.btn_player1_input_attack_num)
        gb.setLayout(box)

        # 전체 배치
        vbox = QVBoxLayout()
        vbox.addLayout(ipbox)       
        vbox.addLayout(infobox)
        self.setLayout(vbox)
        self.show()

    def toggleButton(self, state):
        if state:
            ip = self.ip.text()
            port = self.port.text()
            if self.s.start(ip, int(port)):
                self.btn.setText('서버 종료')                
        else:
            self.s.stop()
            self.result_player2.clear()
            self.btn.setText('서버 실행')

    def updateClient(self):
        self.guest.clearContents()
        QMessageBox.about(self, '알림', '클라이언트와  연결되었습니다')
        i=0
        for ip in self.s.ip:
            self.guest.setItem(i, 0, QTableWidgetItem(ip[0]))
            self.guest.setItem(i, 1, QTableWidgetItem(str(ip[1])))            
            i+=1

    def updateMsg(self):
        self.player1_input_defense_num
    
    def sendMsg(self):
        if not self.s.bListen:
            self.sendmsg.clear()
            return
        self.sendmsg = 'player1가 수비숫자를 입력했습니다'
        self.s.send(self.sendmsg)

        
    def input_player_one_defense_num(self):
        self.player1_defense_num = playerone._input_defense_num_list(self.player1_input_defense_num.text())
        print('player1 수비숫자')
        print(self.player1_defense_num)
        
    def input_wrong_player_one_defense_num(self):
        flag,message = playerone._input_rule_num_list(self.player1_input_defense_num.text())
        QMessageBox.about(self, '알림', message)
        self.player1_input_defense_num.setText('')

    def input_player_one_attack_num(self):
        player1_attack_num = playerone._input_attack_num_list(self.player1_input_attack_num.text())
        game._strikes_and_balls_counter(playerone,playertwo,player1_attack_num)
        playerone_strikes = playerone.strikes
        playerone_balls = playerone.balls
        playerone_trys = playerone.trys
        self.result_player1.append(f'{playerone_trys}차시도')
        self.result_player1.append(f'player1 공격숫자는 {player1_attack_num}입니다.')
        print(f'{self.player2_defense_num}')
        self.result_player1.append(f'결과는 {playerone_strikes}S {playerone_balls}B 입니다')
        self.player1_input_attack_num.setText('')
        if playerone_strikes == 4:
            QMessageBox.about(self, '게임종료', f'    Player1이 승리하였습니다.\n\n     {playerone_trys}번의 시도만에 맞추셨습니다.\n\nPlayer1의 수비숫자는{self.player1_defense_num}입니다.')

    def input_wrong_player_one_attack_num(self):
        flag,message = playerone._input_rule_num_list(self.player1_input_attack_num.text())
        QMessageBox.about(self, '알림', message)
        self.player1_input_attack_num.setText('')
    
