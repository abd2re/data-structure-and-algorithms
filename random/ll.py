class Node:
    def __init__(self,val=None,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Dll:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        if not self.head:
            print('empty list')
            return
        node = self.head
        t = ''
        while node:
            t += str(node.val) + '-->'
            node = node.next
        print(t)

    def print_reverse(self):
        if not self.tail:
            print('empty list')
            return
        node = self.tail
        t = ''
        while node:
            t += str(node.val) + '<--'
            node = node.prev
        print(t)

    def node_beginning(self,val):
        if not self.head:
            node = Node(val)
            self.head = node
            self.tail = node
            return

        node = Node(val,self.head)
        self.head.prev = node
        self.head = node

    def node_end(self,val):
        if not self.head:
            node = Node(val)
            self.head = node
            self.tail = node
            return

        node = Node()



list1 = Dll()


list1.node_beginning('hello')
list1.node_beginning('world')
list1.print()
list1.print_reverse()

