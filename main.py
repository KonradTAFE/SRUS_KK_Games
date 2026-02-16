from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList


player_list = PlayerList()
player_one = Player("1", "a")
player_two = Player("2", "b")
player_list.add_to_start(player_one)
player_list.add_to_tail(player_two)

player_list.display()
player_list.display(False)
