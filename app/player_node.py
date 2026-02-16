from player import Player

class PlayerNode:
    def __init__(self, player: Player):
        self.__player = player
        self.__previous = None
        self.__next = None

    @property
    def player(self):
        return self.__player


    def set_player(self, value: Player):
        self.__player = value

    @property
    def previous(self):
        return self.__previous

    def set_previous(self, value: Player):
        self.__previous = value

    @property
    def next(self):
        return self.__next

    def set_next(self, value: Player):
        self.__next = value

    @property
    def key(self):
        return self.player.uid

    def __str__(self):
        return str(self.player)