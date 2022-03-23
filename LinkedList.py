class Node:
    """
    class to store inverted index data

    Attributes
    ----------
    data : Any
        The data which is suppoused to be stored in the list
        int in inverted index list of docID
        string in inverted index of k-grams
    nextN : Node
        Reference to the next node in the list
    """
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    """
    class to store postinglists

    Attributes
    ----------
    len : length of the posting list

    cursor : current node

    head : Node
        Reference to the first node in the list
    """
    def __init__(self):
        self.head = None
        self.len = 0
        self.cursor = None

    def insert(self, data):
        """
        function to insert node into linkedlist.

        Attributes
        ----------
        data : Any
            The data which is suppoused to be stored in the list
            int in inverted index list of docID
            string in inverted index of k-grams
        
        """
        self.len += 1
        newNode = Node(data)
        if(self.head):
            self.cursor = self.head
            while(self.cursor.next):
                self.cursor = self.cursor.next
            self.cursor.next = newNode
        else:
            self.head = newNode
