from app.player import Player
from app.player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, player: PlayerBNode):
        self.__root = player

    def insert(self, player: Player):
        key = player.name
        if self.__root is None:
            self.__root = PlayerBNode(player)
            return

        if key == self.__root.player.name:
            self.__root.player = player

        elif key > self.__root.player.name:
            if self.__root.right is None:
                self.__root.right = PlayerBST()
            self.__root.right.insert(player)

        else:
            if self.__root.left is None:
                self.__root.left = PlayerBST()
            self.__root.left.insert(player)