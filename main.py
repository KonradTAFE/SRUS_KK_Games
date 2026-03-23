from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList
from app.hash_map import HashMap

player_one = Player("1", "a")
player_two = Player("2", "b")

hash_map = HashMap()
hash_map.put("abc", "abc")
hash_map.put("cba", "cba")
hash_map.put("def", "def")
hash_map.put("fed", "fed")
hash_map.put("ghi", "ghi")
hash_map.put("ihg", "ihg")

print(hash_map.display())
print(repr(player_one))