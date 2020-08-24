
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return self.items

    def peek(self):
        if len(self.items) == 0:
            return []
        return self.items[len(self.items) - 1]

def weav(item1, item2):
    q = Queue()

    while(item1.peek() or item2.peek()):
        if (item1.peek()):
            q.enqueue(item1.dequeue())
        if (item2.peek()):
            q.enqueue(item2.dequeue())
    return q.size()

obj = Queue()
obj1 = Queue()


obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)

obj1.enqueue('Hi')
obj1.enqueue('hello')
obj1.enqueue("There")
obj1.enqueue("How's going mate?")

print(weav(obj, obj1))


