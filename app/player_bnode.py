class PlayerBNode:
    def __init__(self, player):
        self.__player = player
        self.__left = None
        self.__right = None

    @property
    def player(self):
        return self.__player

    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self, right):
        self.__right = right