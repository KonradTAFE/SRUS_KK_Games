import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.new_player = Player("1", "one")

    def test_uid(self):
        self.assertEqual("1", self.new_player.uid)

    def test_name(self):
        self.assertEqual("one", self.new_player.name)

if __name__ == '__main__':
    unittest.main()