class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_forwards(self):
        node = self.head
        if self.head is None:
            print('Linked list is empty')
            return
        t = ''
        while node is not None:
            t = t + str(node.data) + '-->'
            node = node.next

        print(t)

    def print_backwards(self):
        node = self.tail
        if self.tail is None:
            print('Linked list is empty')
            return
        t = ''
        while node is not None:
            t = t + str(node.data) + '<--'
            node = node.prev

        print(t)

    def insert_beginning(self,value):
        if self.head is None:
            newnode = Node(value)
            self.head = newnode
            self.tail = newnode
            return
        node = Node(value,self.head)
        self.head.prev = node
        self.head = node


    def insert_end(self,value):
        if self.tail is None:
            newnode = Node(value)
            self.tail = newnode
            self.head = newnode
            return
        node = Node(value,None,self.tail)
        self.tail.next = node
        self.tail = node

    def insert_afternode(self,val,afternode):
        if self.head is None:
            print('linked list is empty')
        if self.tail == afternode:
            self.insert_end(val)
            return
        newnode = Node(val,afternode.next,afternode)
        afternode.next = newnode
        newnode.next.prev = newnode

    def insert_beforenode(self,val,beforenode):
        if self.tail is None:
            print('linked list is empty')
        if self.head == beforenode:
            self.insert_beginning(val)
            return
        newnode = Node(val,beforenode,beforenode.prev)
        beforenode.prev = newnode
        newnode.prev.next = newnode


liste = DoubleLinkedList()
liste.insert_beginning('hello')
liste.insert_beginning('world')
liste.insert_end('test')
liste.insert_end('works')
liste.insert_afternode('im in',liste.head.next.next)
liste.insert_beforenode('im here too',liste.head.next)

liste.print_forwards()
liste.print_backwards()



