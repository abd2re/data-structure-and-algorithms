from collections import deque
import time
import threading


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,data):
        self.buffer.appendleft(data)

    def deque(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)


system = Queue()
orders = ['pizza','samosa','pasta','biryani','burger']

def place_order(*orders):
    for order in orders:
        system.enqueue(order)
        print(f'{order} has been added. Queue: {list(system.buffer)}')
        time.sleep(0.5)

def serve_order():
    while system.buffer:
        print(f'--> {system.deque()} has been served. Queue: {list(system.buffer)}')
        time.sleep(2)




t1 = threading.Thread(target=place_order,args=orders)
t2 = threading.Thread(target=serve_order)

t1.start()
time.sleep(1)
t2.start()

#t1.join()
#t2.join()
