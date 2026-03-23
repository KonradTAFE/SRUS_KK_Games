import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.new_player = Player("1", "one")

    def test_uid(self):
        self.assertEqual("1", self.new_player.uid)

    def test_name(self):
        self.assertEqual("one", self.new_player.name)

    def test_sort_players(self):
        players = [Player(name="Alice", uid='01', score=10), Player(name="Bob", uid='02', score=5),
                   Player(name="Charlie", uid='03', score=15)]

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player(name="Bob", uid='02', score=5), Player(name="Alice", uid='01', score=10),
                                   Player(name="Charlie", uid='03', score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_sort_with_classmethod(self):
        players = [Player(name="Alice", uid='01', score=10), Player(name="Bob", uid='02', score=5),
                   Player(name="Charlie", uid='03', score=15)]

        # do **not** change the following code:
        sorted_players = Player.sort_quickly(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player(name="Charlie", uid='03', score=15), Player(name="Alice", uid='01', score=10), Player(name="Bob", uid='02', score=5)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player(name="Alice", uid='01', score=10)
        bob = Player(name="Bob", uid='02', score=5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(alice > bob)
        # or, event better
        self.assertGreater(alice, bob)

if __name__ == '__main__':
    unittest.main()