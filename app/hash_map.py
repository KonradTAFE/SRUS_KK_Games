from player_list import PlayerList

class HashMap():
    def __init__(self, max_size = 10):
        self.__current_size = 0
        self.max_size = max_size
        self.__table = []
        for _ in range(max_size):
            self.__table.append(PlayerList)

    def is_full(self):
        return self.__current_size == self.max_size

    def put(self, key, name):
        pass

    def get(self, key):
        pass

    def remove(self, key):
        pass

    def size(self) -> int:
        return self.__current_size