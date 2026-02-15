import unittest
from app.player_node import PlayerNode
from app.player_list import PlayerList
from player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.new_list = PlayerList()

    def test_add_when_empty(self):
        new_player = Player("123", "abc")
        self.new_list.add_to_start(new_player)
        self.assertEqual(new_player, self.new_list.head.player)

    def test_add_when_not_empty(self):
        #create an initial head and add it to the list
        head = Player("987", "xyz")
        self.new_list.add_to_start(head)
        #create a new player and add it to start
        new_player = Player("123", "abc")
        self.new_list.add_to_start(new_player)
        #compare the initial head's name with the new_player next's name
        self.assertEqual(head.name, self.new_list.head.next.player.name)

if __name__ == '__main__':
    unittest.main()