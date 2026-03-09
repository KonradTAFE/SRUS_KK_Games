import unittest
from app.hash_map import HashMap
from app.player import Player
from app.player_node import PlayerNode


class TestHashMap(unittest.TestCase):

    def setUp(self):
        self.hash_map = HashMap()
        self.hash_map.put("abc", "test1")

    def test_put(self):
        self.assertEqual(self.hash_map.size(), 1)
        self.hash_map.put("abc", "test2")
        index = self.hash_map.get_index("abc")
        self.assertEqual(self.hash_map.table[index].find_key("abc").name, "test2")
        self.assertEqual(self.hash_map.size(), 1)
        self.hash_map.put("def", "test3")
        self.assertEqual(self.hash_map.size(), 2)

    def test_get(self):
        # get the name of player with key "abc" and compare with "test1"
        self.assertEqual(self.hash_map.get("abc").name, "test1")
        # confirm the function returns None if not found
        self.assertEqual(self.hash_map.get("cba"), None)

    def test_remove(self):
        self.assertEqual(self.hash_map.size(), 1)
        self.hash_map.remove("abc")
        self.assertEqual(self.hash_map.size(), 0)
        # removing from empty list / key not found
        self.assertEqual(self.hash_map.remove("abc"), None)