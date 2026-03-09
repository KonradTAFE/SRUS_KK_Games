import unittest
from app.hash_map import HashMap
from app.player import Player
from app.player_node import PlayerNode


class TestHashMap(unittest.TestCase):

    def setUp(self):
        self.hash_map = HashMap()
        self.hash_map.put("abc", "Konrad")

    def test_put(self):
        self.assertEqual(self.hash_map.current_size, 1)
        self.hash_map.put("abc", "Marcos")
        index = self.hash_map.get_index("abc")
        self.assertEqual(self.hash_map.table[index].find_key("abc").name, "Marcos")
        self.assertEqual(self.hash_map.current_size, 1)
        self.hash_map.put("def", "Juan")
        self.assertEqual(self.hash_map.current_size, 2)
