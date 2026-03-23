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

    @classmethod
    def sort_quickly(cls, player_list):
        if len(player_list) <= 1:
            return player_list
        middle = len(player_list)//2
        pivot = player_list[middle]
        left = player_list[:middle]
        right = player_list[middle + 1 :]
        low = 0
        high = len(right)-1
        for x in player_list:
            if x > pivot:
                left.append(x)
            else:
                right.append(x)


        return cls.sort_quickly(left) + [pivot] + cls.sort_quickly(right)

    def __hash__(self, size: int):
        return self.hash_function(self.uid, size)

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __str__(self):
        # returns player as a string
        return f"Player {self.uid} - {self.name} - score: {self.score}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', uid='{self.uid}', score='{self.score}')"