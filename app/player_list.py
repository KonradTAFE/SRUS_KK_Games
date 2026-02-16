from player import Player
from player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        return self.__head

    def set_head(self, value: PlayerNode):
        self.__head = value

    @property
    def tail(self):
        return self.__tail

    def set_tail(self, value: PlayerNode):
        self.__tail = value

    def is_empty(self) -> bool:
        return self.head is None

    def add_to_start(self, player: Player):
        new_player = PlayerNode(player)
        if self.is_empty():
            self.set_head(new_player)
            self.set_tail(new_player)
            return
        self.head.set_previous(new_player)
        new_player.set_next(self.head)
        self.set_head(new_player)

    def add_to_tail(self, player: Player):
        new_player = PlayerNode(player)
        if self.is_empty():
            self.set_head(new_player)
            self.set_tail(new_player)
            return
        self.tail.set_next(new_player)
        new_player.set_previous(self.tail)
        self.set_tail(new_player)

    def delete_head(self):
        if self.is_empty():
            return None
        if self.head.next is None:
            self.set_head(None)
            return self.head
        else:
            self.head.next.set_previous(None)
            self.set_head(self.head.next)
            return self.head

    def delete_tail(self):
        if self.is_empty():
            return None
        if self.tail.previous is None:
            self.set_tail(None)
            return self.tail
        else:
            self.tail.previous.set_next(None)
            self.set_tail(self.tail.previous)
            return self.tail

    def delete_key(self, key: str):
        current = self.head
        previous = self.head
        while current.player.uid != key:
            if current.next is None:
                return None
            else:
                previous = current
                current = current.next
        if current == self.head:
            self.set_head(self.head.next)
            self.head.set_previous(None)
        else:
            previous.set_next(current.next)
            current.set_previous(previous)
        return current

    def display(self, forward = True):
        if forward:
            print("Player list from the start:")
            current = self.head
            while current is not None:
                print(current)
                current = current.next
        else:
            print("Player list from the end:")
            current = self.tail
            while current is not None:
                print(current)
                current = current.previous