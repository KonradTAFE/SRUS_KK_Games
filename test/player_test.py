import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):

    def test_uid(self):
        new_player = Player("1", "one")
        self.assertEqual("1", new_player.uid)

    def test_name(self):
        new_player = Player("1", "one")
        self.assertEqual("one", new_player.name)
