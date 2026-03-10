import unittest
from app.hash_map import HashMap
from app.player import Player
from app.player_node import PlayerNode


class TestHashMap(unittest.TestCase):

    def setUp(self):
        self.hash_map = HashMap()
        self.hash_map.put("abc", "test1")

    def test_put(self):
        # test the size of the map before operations
        self.assertEqual(self.hash_map.size(), 1)
        # test put function with the same key
        self.hash_map.put("abc", "test2")
        index = self.hash_map.get_index("abc")
        # confirm the name has been updated
        self.assertEqual(self.hash_map.table[index].find_key("abc").name, "test2")
        # confirm the size is still the same
        self.assertEqual(self.hash_map.size(), 1)
        # put a new player into the map
        self.hash_map.put("def", "test3")
        # confirm the size was updated
        self.assertEqual(self.hash_map.size(), 2)

    def test_get(self):
        # get the name of player with key "abc" and compare with "test1"
        self.assertEqual(self.hash_map.get("abc").name, "test1")
        # confirm the function returns None if not found
        self.assertEqual(self.hash_map.get("cba"), None)

    def test_remove(self):
        # confirm the size before operations
        self.assertEqual(self.hash_map.size(), 1)
        # remove the key "abc"
        self.hash_map.remove("abc")
        # confirm the size is down to 0
        self.assertEqual(self.hash_map.size(), 0)
        # removing from empty list / key not found
        self.assertEqual(self.hash_map.remove("abc"), None)