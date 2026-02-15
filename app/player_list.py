from player import Player
from player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        return self.__head

    def set_head(self, value: PlayerNode):
        self.__head = value

    @property
    def tail(self):
        return self.__tail

    def set_tail(self, value: PlayerNode):
        self.__tail = value

    def is_empty(self) -> bool:
        return self.head is None

    def add_to_start(self, player: Player):
        new_player = PlayerNode(player)
        if self.is_empty():
            self.set_head(new_player)
            self.set_tail(new_player)
            return

        self.head.set_previous(new_player)
        new_player.set_next(self.head)
        self.set_head(new_player)

