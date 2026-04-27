class PlayerBNode:
    def __init__(self, player):
        self.__player = player
        self.__left = None
        self.__right = None

    @property
    def player(self):
        return self.__player
    @player.setter
    def player(self, player):
        self.__player = player

    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, player):
        self.__left = player

    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self, player):
        self.__right = player