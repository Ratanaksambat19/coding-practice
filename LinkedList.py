class Node:
    
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def insertFirst(self, data):
        self.head = Node(data, self.head)

    def size(self):
        counter = 0
        node = self.head
        while (node.next):
            counter += 1
            node = node.next
        return counter
            
    def getFirst(self):
        return self.getAt(0)

    def getLast(self):
        # if (self.head == None):
        #     return None

        # node = self.head
        # while(node):
        #     if (node.next == None):
        #         return node
        #     node = node.next
        # return node
        return self.getAt(self.size() - 1)

    def clear(self):
        self.head = None

    def removeFirst(self):
        if self.head == None:
            return None
        self.head = self.head.next

    def removeLast(self):
        if (self.head == None):
            return 
        if (self.head.next == None):
            self.head = None
            return
        
        previous = self.head
        node = self.head.next
        while(node.next):
            previous = node
            node = node.next
        previous.next = None

    def insertLast(self, data):
        last = self.getLast()
        if (last):
            last.next = Node(data)
        else:
            self.head = Node(data) 

    def getAt(self, idx):
        node = self.head
        counter = 0
        while(node):
            if idx == counter:
                return node
            node = node.next
            counter += 1
        return None

    def removeAt(self, idx):
        if(self.head == None):
            return
        if(idx == 0):
            self.head = self.head.next
            return
        
        previous_node = self.getAt(idx - 1)
        if(previous_node == None and previous_node.next == None):
            return
        previous_node.next = previous_node.next.next

    def insertAt(self, data, idx):
        node = self.getAt(idx)

        if (self.head == None):
            self.head = Node(data)
            return 

        if (idx == 0):
            self.head = Node(data, self.head)
            return 
        
        previous_node = self.getAt(idx - 1) or self.getLast()
        node =  Node(data, previous_node.next)
        previous_node.next = node

    def listPrint(self):
        printval = self.head
        
        while (printval is not None):
            print(printval.data)
            printval = printval.next

    # def forEach(fn):


if __name__ == "__main__":
    lst = LinkedList()
    lst.head = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    lst.head.next = e2
    e2.next = e3
    lst.insertFirst("sun")
    lst.insertAt("holiday", 3)
    lst.removeAt(3)
    lst.insertFirst("Tuesday")
    print(lst.getLast())
    print(lst.listPrint())