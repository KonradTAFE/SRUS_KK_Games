class Player:
    def __init__(self, uid: str, name: str, score: int = 0):
        self.__uid = uid
        self.__name = name
        self.__score = score

    @property
    def uid(self):
        # returns the player id
        return self.__uid

    @property
    def name(self):
        # returns the player name
        return self.__name

    @property
    def score(self):
        # returns the player's score
        return self.__score

    @score.setter
    def score(self, score: int):
        if score < 0:
            raise ValueError("Score cannot be negative")
        else:
            self.__score = score

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
        return self.hash_function(self.uid, size)

    def __eq__(self, other):
        return self.uid == other.uid

    def __str__(self):
        # returns player as a string
        return f"Player {self.uid} - {self.name} - score: {self.score}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', uid='{self.uid}', score='{self.score}')"