class Node:
    def __init__(self, data, nextN=None):
        self.next = nextN
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0
        self.cursor = None

    def insert(self, data):
        self.len = self.len + 1
        if self.head is None:
            self.head = Node(data)
            self.cursor = self.head
        else:
            self.cursor.next = Node(data)
