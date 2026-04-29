import unittest

from app.player import Player
from app.player_bst import PlayerBST


class TestPlayerBST(unittest.TestCase):
    def setUp(self):
        self.my_bst = PlayerBST()
        self.player_a = Player("A", "1")
        self.player_b = Player("B", "2")
        self.player_c = Player("C", "3")
        self.player_b_updated = Player("B", "4")

    def test_add_to_new_BST(self):
        self.my_bst.insert(self.player_a)
        self.assertEqual(self.my_bst.root.player, self.player_a)

    def test_add_to_right(self):
        self.my_bst.insert(self.player_b)
        self.my_bst.insert(self.player_c)
        self.assertEqual(self.my_bst.root.player, self.player_b)
        self.assertEqual(self.my_bst.root.right.root.player, self.player_c)

    def test_add_to_left(self):
        self.my_bst.insert(self.player_b)
        self.my_bst.insert(self.player_a)
        self.assertEqual(self.my_bst.root.player, self.player_b)
        self.assertEqual(self.my_bst.root.left.root.player, self.player_a)

    def test_update_value(self):
        self.my_bst.insert(self.player_b)
        self.my_bst.insert(self.player_b_updated)
        self.assertEqual(self.my_bst.root.player, self.player_b_updated)

    def test_search_empty(self):
        result = self.my_bst.search(self.player_b)
        self.assertEqual(result, None)

    def test_search_not_empty(self):
        self.my_bst.insert(self.player_b)
        self.my_bst.insert(self.player_a)
        self.my_bst.insert(self.player_c)
        result_a = self.my_bst.search("1")
        self.assertEqual(result_a, self.player_a)
        result_c = self.my_bst.search("3")
        self.assertEqual(result_c, self.player_c)

    def test_balance(self):
        self.my_bst.insert(self.player_a)
        self.my_bst.insert(self.player_b)
        self.my_bst.insert(self.player_c)
        balanced = self.my_bst.balance()
        self.assertEqual(balanced.root.player.name, "2")
        self.assertEqual(balanced.root.left.root.player.name, "1")
        self.assertEqual(balanced.root.right.root.player.name, "3")