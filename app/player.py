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

    def __str__(self):
        # returns player as a string
        return "Player " + self.uid + " - " + self.name