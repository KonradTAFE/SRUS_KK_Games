from app.player import Player

class PlayerNode:
    def __init__(self, player: Player):
        self.__player = player
        self.__previous = None
        self.__next = None

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, value: Player):
        self.__player = value

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, value: Player):
        self.__previous = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value: Player):
        self.__next = value

    @property
    def key(self):
        return self.player.uid

    def __str__(self):
        return str(self.player)