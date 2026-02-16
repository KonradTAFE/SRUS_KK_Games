import unittest
from app.player_list import PlayerList
from app.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.new_list = PlayerList()
        self.player_one = Player("1", "a")
        self.player_two = Player("2", "b")
        self.player_three = Player("3", "c")

    def test_add_head_to_empty(self):
        self.new_list.add_to_start(self.player_one)
        self.assertEqual(self.player_one, self.new_list.head.player)

    def test_add_head_to_not_empty(self):
        self.new_list.add_to_start(self.player_one)
        self.new_list.add_to_start(self.player_two)
        #compare the initial head's name with the new_player next's name
        self.assertEqual(self.player_one.name, self.new_list.head.next.player.name)

    def test_add_tail_to_empty(self):
        self.new_list.add_to_tail(self.player_one)
        self.assertEqual(self.player_one, self.new_list.tail.player)

    def test_add_tail_to_not_empty(self):
        self.new_list.add_to_tail(self.player_one)
        self.assertEqual(self.player_one, self.new_list.tail.player)
        self.new_list.add_to_tail(self.player_two)
        self.assertEqual(self.new_list.tail.player, self.player_two)

    def test_delete_head_from_empty(self):
        self.assertEqual(self.new_list.delete_head(), None)

    def test_delete_head(self):
        self.new_list.add_to_start(self.player_one)
        self.new_list.add_to_tail(self.player_two)
        self.new_list.delete_head()
        self.assertEqual(self.player_two, self.new_list.head.player)

    def test_delete_tail(self):
        self.new_list.add_to_start(self.player_one)
        self.new_list.add_to_tail(self.player_two)
        self.new_list.delete_tail()
        self.assertEqual(self.player_one, self.new_list.tail.player)

    def test_delete_key(self):
        self.new_list.add_to_start(self.player_one)
        self.new_list.add_to_tail(self.player_two)
        self.new_list.delete_key(self.player_one.uid)
        self.assertEqual(self.player_two, self.new_list.head.player)
        self.assertEqual(self.player_two, self.new_list.tail.player)

if __name__ == '__main__':
    unittest.main()