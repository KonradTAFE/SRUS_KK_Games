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
            return
        elif key > self.__root.player.name:
            if self.__root.right is None:
                self.__root.right = PlayerBST()
            self.__root.right.insert(player)
            return
        else:
            if self.__root.left is None:
                self.__root.left = PlayerBST()
            self.__root.left.insert(player)


    def search(self, name):
        if self.__root is None:
            return None
        if self.__root.player.name == name:
            return self.__root.player
        if name > self.__root.player.name:
            if self.__root.right is None:
                return None
            else:
                return self.__root.right.search(name)
        else:
            if self.__root.left is None:
                return None
            else:
                return self.__root.left.search(name)

    def tree_to_list(self):
        bst_list = []
        self.add_to_list(self, bst_list)
        return bst_list

    def add_to_list(self, tree, new_list):
        if tree is None or tree.root is None:
            return
        self.add_to_list(tree.root.left, new_list)
        new_list.append(tree.root.player)
        self.add_to_list(tree.root.right, new_list)

    def build_balance(self, players_list):
        if not players_list:
            return None

        mid = len(players_list) // 2
        balanced_bst = PlayerBST()
        balanced_bst.root = PlayerBNode(players_list[mid])
        balanced_bst.root.left = self.build_balance(players_list[:mid])
        balanced_bst.root.right = self.build_balance(players_list[mid + 1:])
        return balanced_bst

    def balance(self):
        sorted_players_list = self.tree_to_list()
        return self.build_balance(sorted_players_list)