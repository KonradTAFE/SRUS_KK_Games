from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        # returns the first player
        return self.__head

    def set_head(self, value: PlayerNode):
        # new head setter
        self.__head = value

    @property
    def tail(self):
        # returns the last player
        return self.__tail

    def set_tail(self, value: PlayerNode):
        # new tail setter
        self.__tail = value

    def is_empty(self) -> bool:
        return self.head is None

    def add_to_start(self, player: Player):
        # create new player node with passed player data
        new_player = PlayerNode(player)
        # if the list is empty, assign the new node as the list's head and tail
        if self.is_empty():
            self.set_head(new_player)
            self.set_tail(new_player)
            return
        # if not empty:
            # assign the new player as a previous for old head
        self.head.set_previous(new_player)
            # assign the old head as the new player's next
        new_player.set_next(self.head)
            # assign the new player as the list's head
        self.set_head(new_player)

    def add_to_tail(self, player: Player):
        # create new player node with passed player data
        new_player = PlayerNode(player)
        # if the list is empty, assign the new node as the list's head and tail
        if self.is_empty():
            self.set_head(new_player)
            self.set_tail(new_player)
            return
        # if not empty:
            # assign the new player as a next for old tail
        self.tail.set_next(new_player)
            # assign the old tail as the new player's previous
        new_player.set_previous(self.tail)
            # assign the new player as the list's tail
        self.set_tail(new_player)

    def delete_head(self):
        # if empty, return nothing
        if self.is_empty():
            return None
        # if only one item, set head to none and return
        if self.head.next is None:
            self.set_head(None)
            return self.head
        # if more than one item:
        else:
            # delete the second item's previous
            self.head.next.set_previous(None)
            # set second item as head
            self.set_head(self.head.next)
            return self.head

    def delete_tail(self):
        # if empty, return nothing
        if self.is_empty():
            return None
        # if only one item, set head to none and return
        if self.tail.previous is None:
            self.set_tail(None)
            return self.tail
        # if more than one item:
        else:
            # delete the second from end item's next
            self.tail.previous.set_next(None)
            # set second from end item as tail
            self.set_tail(self.tail.previous)
            return self.tail

    def delete_key(self, key: str):
        # create dummy variables for reassigning purposes
        current = self.head
        previous = self.head
        # travers through the list to find the key
        while current.player.uid != key:
            # if key not found, return None
            if current.next is None:
                return None
            else:
                previous = current
                current = current.next
        # if the key is found and the node is the head, reassign the head to the next item
        if current == self.head:
            self.set_head(self.head.next)
            self.head.set_previous(None)
        # if the key is not the head, reassign the connections
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