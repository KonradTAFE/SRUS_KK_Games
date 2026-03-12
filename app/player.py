class Player:
    def __init__(self, uid: str, name: str):
        self.__uid = uid
        self.__name = name

    @property
    def uid(self):
        # returns the player id
        return self.__uid

    @property
    def name(self):
        # returns the player name
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @classmethod
    def hash_function(cls, key: str, size: int) -> int:
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % size

    def __hash__(self, size: int):
        return self.hash_function(self.uid) % size

    def __eq__(self, other):
        return self.uid == other.uid

    def __str__(self):
        # returns player as a string
        return "Player " + self.uid + " - " + self.name