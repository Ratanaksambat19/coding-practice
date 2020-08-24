class Stack:

    def __init__(self):
        self.container = []

    def push(self, elem):
        self.container.append(elem)

    def pop(self):
        if len(self.container) != 0:
            return self.container.pop()
        return []

    def peek(self):
        if len(self.container) != 0:
            return self.container[-1]
        return []

    def show(self):
        return self.container

class QueueStack:

    def __init__(self):
        self.origin_container = Stack()
        self.backup_container = Stack()

    def push(self, elem):
        self.origin_container.push(elem)

    def arr(self):
        return self.origin_container.show()

    def peek(self):
        while self.origin_container.peek():
            self.backup_container.push(self.origin_container.pop())
        record = self.backup_container.pop()

        while self.backup_container.peek():
            self.origin_container.push(self.backup_container.pop())
        
        return record

    def pop(self):
        while self.origin_container.peek():
            self.backup_container.push(self.origin_container.pop())
        record = self.backup_container.pop()

        while self.backup_container.peek():
            self.origin_container.push(self.backup_container.pop())
        return record

    def show(self):
        return self.origin_container.show()
    
    

obj = QueueStack()
# obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)

print(obj.arr())
print(obj.pop())
print(obj.peek())
print(obj.show())
        