class Stack:
    def __init__(self):
        self.__data = []

    @property
    def data(self):
        return self.__data

    def __repr__(self) -> str:
        return f"{self.__data}"

    def push(self, value):
        self.__data.append(value)

    def pop(self):
        try:
            value = self.__data[-1]
            del self.__data[-1]
            return value
        except IndexError:
            return None

class AdvansedStack(Stack):
    def __len__(self):
        return len(self.data)

stack1 = Stack()
stack2 = AdvansedStack()

stack1.push(1)
stack1.push('f')
stack1.push(2.4)

print(stack1)
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
print(stack1)

stack2.push('ddd')
stack2.push(33)
stack2.push('dfwe5345')
print(stack2)
stack2.pop()
print(stack2)
print(len(stack2))