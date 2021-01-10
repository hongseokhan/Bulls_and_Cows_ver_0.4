from player import Player
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtCore

class Human(Player):
    
    def __init__(self):
        super().__init__()
        
    def _input_rule_num_list(self,num_list):
        flag = True
        message = []
        if not(num_list.isdecimal()):
            flag = False
            message = f'{num_list}는 숫자가 아닙니다.'

        elif len(num_list) != 4:
            flag = False
            message = f'{num_list}는 4자리 숫자가 아닙니다.'
            
        elif len(num_list) != len(set(num_list)):
            flag = False
            message = f'{num_list}는 중복된 숫자가 존재 합니다'
        return flag, message
    
    def _input_defense_num_list(self,player_input_defense_num):
        flag = False
        while flag is False:
            self._defense_num_list = player_input_defense_num
            flag, message = self._input_rule_num_list(self._defense_num_list)
            if flag is False:
                print(message)
            else:
                return self._defense_num_list
            break
    
    def _input_attack_num_list(self,player_input_attack_num):
        flag = False
        
        while flag is False:
            attack_num_list = player_input_attack_num
            flag, message = self._input_rule_num_list(attack_num_list)
            if flag is False:
                print(message)
            else:
                return attack_num_list
            break