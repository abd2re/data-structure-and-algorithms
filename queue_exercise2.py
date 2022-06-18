from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def deque(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]


q = Queue()
q.enqueue('1')

for i in range(10):
    print(q.front())
    q.enqueue(q.front() + '0')
    q.enqueue(q.front() + '1')
    q.deque()

