class Player:
    
    def __init__(self):
        self.__strikes = 0
        self.__balls = 0 
        self.__trys = 0
        self._defense_num_list = []

    @property
    def strikes(self):
        return self.__strikes
    
    @strikes.setter
    def strikes(self,strikes):
        self.__strikes = strikes

    @property
    def balls(self):
        return self.__balls
    
    @balls.setter
    def balls(self,balls):
        self.__balls = balls
    
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self,score):
        self.__score = score
    
    @property
    def trys(self):
        return self.__trys
    
    @trys.setter
    def trys(self,trys):
        self.__trys = trys

    @property
    def defense_num_list(self):
        return self._defense_num_list
    
    @defense_num_list.setter
    def defense_num_list(self,defense_num_list):
        self._defense_num_list = defense_num_list
    