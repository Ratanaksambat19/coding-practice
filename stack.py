class Stack:

    def __init__(self):
        self.container = []

    def push(self, elem):
        self.container.append(elem)

    def pop(self):
        return self.container.pop()

    def peeK(self):
        return self.container[-1]

    def show(self):
        return self.container

obj = Stack()

obj.push(5)
obj.push(3)
obj.push(4)

print(obj.pop())
print(obj.show())
print(obj.peeK())