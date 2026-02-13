from player import Player
from player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.__head = None

    @property
    def head(self):
        return self.__head

    def is_empty(self) -> bool:
        return self.__head is None

    def add_to_start(self, player: Player):
        new_player = PlayerNode(player)
        if self.is_empty():
            self.__head = new_player
        else:
            self.__head.set_previous = new_player
            new_player.set_next = self.__head
            self.__head = new_player
