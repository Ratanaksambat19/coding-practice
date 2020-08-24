class Node:
    
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def insertFirst(self, data):
        self.head = Node(data, self.head)

    # def size(self):

node = Node(2)
obj = LinkedList()
obj.head = node
obj.insertFirst(5)
obj.insertFirst(6)
obj.insertFirst(7)

print(obj)