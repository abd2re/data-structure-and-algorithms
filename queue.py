from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def deque(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)


pq = Queue()

pq.enqueue({
    'crypto' : 'bitcoin',
    'price' : 20000,
    'time' : '13:30'
})

pq.enqueue({
    'crypto' : 'ethereum',
    'price' : 999,
    'time' : '13:50'
})

pq.enqueue({
    'crypto' : 'cardano',
    'price' : 1,
    'time' : '14:10'
})


print(pq.buffer)

pq.deque()

print(pq.buffer)