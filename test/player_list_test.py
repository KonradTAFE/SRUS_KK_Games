import unittest
from app.player_list import PlayerList
from app.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.new_list = PlayerList()

    def test_add_head_to_empty(self):
        new_player = Player("123", "abc")
        self.new_list.add_to_start(new_player)
        self.assertEqual(new_player, self.new_list.head.player)

    def test_add_head_to_not_empty(self):
        #create an initial head and add it to the list
        head = Player("987", "xyz")
        self.new_list.add_to_start(head)
        #create a new player and add it to start
        new_player = Player("123", "abc")
        self.new_list.add_to_start(new_player)
        #compare the initial head's name with the new_player next's name
        self.assertEqual(head.name, self.new_list.head.next.player.name)

    def test_add_tail_to_empty(self):
        new_player = Player("123", "abc")
        self.new_list.add_to_tail(new_player)
        self.assertEqual(new_player, self.new_list.tail.player)

    def test_add_tail_to_not_empty(self):
        tail = Player("987", "xyz")
        self.new_list.add_to_tail(tail)
        self.assertEqual(tail, self.new_list.tail.player)
        new_player = Player("123", "abc")
        self.new_list.add_to_tail(new_player)
        self.assertEqual(self.new_list.tail.player, new_player)

    def test_delete_head_from_empty(self):
        self.assertEqual(self.new_list.delete_head(), None)

    def test_delete_head(self):
        player_one = Player("1", "a")
        player_two = Player("2", "b")
        self.new_list.add_to_start(player_one)
        self.new_list.add_to_tail(player_two)
        self.new_list.delete_head()
        self.assertEqual(player_two, self.new_list.head.player)

    def test_delete_tail(self):
        player_one = Player("1", "a")
        player_two = Player("2", "b")
        self.new_list.add_to_start(player_one)
        self.new_list.add_to_tail(player_two)
        self.new_list.delete_tail()
        self.assertEqual(player_one, self.new_list.tail.player)

    def test_delete_key(self):
        player_one = Player("1", "a")
        player_two = Player("2", "b")
        self.new_list.add_to_start(player_one)
        self.new_list.add_to_tail(player_two)
        self.new_list.delete_key("1")
        self.assertEqual(player_two, self.new_list.head.player)
        self.assertEqual(player_two, self.new_list.tail.player)

if __name__ == '__main__':
    unittest.main()