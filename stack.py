from collections import deque

stack = deque()

stack.append('1')
stack.append('2')
stack.append('3')
stack.pop()

print(stack)


class Stack:
    def __init__(self):
        self.containter = deque()

    def push(self,val):
        self.containter.append(val)

    def pop(self):
        return self.containter.pop()

    def peek(self):
        return self.containter[-1]

    def is_empty(self):
        return len(self.containter)==0

    def size(self):
        return len(self.containter)


stack1 = Stack()

stack1.push('hello')
stack1.push('world')

print(stack1.peek())