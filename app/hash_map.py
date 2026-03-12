from app.player import Player
from app.player_list import PlayerList


class HashMap:
    def __init__(self, max_size:int = 10):
        self.__max_size = max_size
        self.table = []
        for _ in range(max_size):
            self.table.append(PlayerList())

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.__max_size
        else:
            return Player.hash_function(key, self.__max_size)

    def put(self, key: str, name: str):
        index = self.get_index(key)
        player_list = self.table[index]
        if player_list.find_key(key) is None:
            player_list.add_to_tail(Player(key, name))
            return
        player = player_list.find_key(key)
        player.name = name


    def get(self, key: str) -> Player | None:
        index = self.get_index(key)
        player_list = self.table[index]
        if player_list.find_key(key) is None:
            return None
        else:
            return player_list.find_key(key)

    def remove(self, key: str):
        player_list = self.table[self.get_index(key)]
        player = self.get(key)
        if player is None:
            print("Player not found")
            return None
        else:
            player_list.delete_key(key)
            print(f"{player} removed!")
            return player

    def size(self) -> int:
        current_size = 0
        for _ in self.table:
            current = _.head
            while current is not None:
                current_size += 1
                current = current.next
        return current_size

    def display(self):
        display_string = ""
        for _ in self.table:
            display_string += "Index " + str(self.table.index(_)) + ":\n"
            current = _.head
            while current is not None:
                display_string += "    " + str(current.player) + "\n"
                current = current.next
            display_string += "\n"
        return display_string