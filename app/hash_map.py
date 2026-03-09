from app.player import Player
from app.player_list import PlayerList


class HashMap:
    def __init__(self, size = 10):
        self.current_size = 0
        self.__max_size = size
        self.table = []
        for _ in range(size):
            self.table.append(PlayerList())

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.size()
        else:
            return Player.hash_function(key) % self.size()

    def put(self, key: str, name: str):
        index = self.get_index(key)
        player_list = self.table[index]
        if player_list.find_key(key) is None:
            player_list.add_to_tail(Player(key, name))
            self.current_size += 1
            return
        player = player_list.find_key(key)
        player.name = name


    def get(self, key):
        pass

    def remove(self, key):
        pass

    def size(self) -> int:
        return self.__max_size