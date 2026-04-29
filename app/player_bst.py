from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    """
    A Binary Search Tree (BST) implementation for storing Player objects.

    The tree is organized by player name (string comparison).
    Each node contains a PlayerBNode, and its left and right children
    are themselves PlayerBST instances.
    """

    def __init__(self):
        self.__root = None

    @property
    def root(self):
        """
        Gets the root node of the BST.

        Returns:
            PlayerBNode: The root node of the tree.
        """
        return self.__root

    @root.setter
    def root(self, player: PlayerBNode):
        """
        Sets the root node of the BST.

        Args:
            player (PlayerBNode): The node to set as root.
        """
        self.__root = player

    def insert(self, player: Player):
        """
        Inserts a Player into the BST based on their name.

        If a player with the same name already exists, it is replaced.

        Args:
            player (Player): The player to insert.
        """
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
        """
        Searches for a Player by name in the BST.

        Args:
            name (str): The name of the player to search for.

        Returns:
            Player or None: The matching Player object if found,
            otherwise None.
        """
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
        """
        Helper function for the balance method.
        Converts the BST into a sorted list of Player objects.

        Uses in-order traversal to ensure the list is sorted
        by player name.

        Returns:
            list[Player]: A sorted list of players.
        """
        bst_list = []
        self.add_to_list(self, bst_list)
        return bst_list

    def add_to_list(self, tree, new_list):
        """
        Helper function for the balance method.
        Performs in-order traversal and appends players to a list.

        Args:
            tree (PlayerBST): The current subtree being traversed.
            new_list (list): The list to append Player objects to.
        """
        if tree is None or tree.root is None:
            return

        self.add_to_list(tree.root.left, new_list)
        new_list.append(tree.root.player)
        self.add_to_list(tree.root.right, new_list)

    def build_balance(self, players_list):
        """
        Builds a balanced BST from a sorted list of Player objects.

        The middle element of the list becomes the root,
        and the process is applied recursively to left and right lists.

        Args:
            players_list (list[Player]): A sorted list of players.

        Returns:
            PlayerBST or None: A balanced BST or None.
        """
        if not players_list:
            return None

        mid = len(players_list) // 2

        balanced_bst = PlayerBST()
        balanced_bst.root = PlayerBNode(players_list[mid])

        balanced_bst.root.left = self.build_balance(players_list[:mid])
        balanced_bst.root.right = self.build_balance(players_list[mid + 1:])

        return balanced_bst

    def balance(self):
        """
        Balances the current BST.

        Converts the tree into a sorted list and rebuilds it
        into a balanced BST.

        Returns:
            PlayerBST: A new balanced BST.
        """
        sorted_players_list = self.tree_to_list()
        return self.build_balance(sorted_players_list)