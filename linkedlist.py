class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        node = self.head
        if self.head is None:
            print('Linked list is empty')
            return
        t = ''
        while node is not None:
            t = t + str(node.val) + '-->'
            node = node.next
        print(t)
        return

    def insert_beginning(self,newval):
        newnode = Node(newval,self.head)
        self.head = newnode

    def insert_afternode(self,newval,node):
        if node is None:
            print("node doesn't exist")
            return
        newnode = Node(newval,node.next)
        node.next = newnode
        return

    def insert_end(self,newval):
        if self.head is None:
            self.head = Node(newval)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(newval)

    def paste_arr(self,arr):
        #self.head = None
        for i in arr:
            self.insert_end(i)

    def get_length(self):
        c = 0
        if self.head is None:
            return c
        node = self.head
        while node:
            c+=1
            node = node.next
        return c

    def remove_elems(self,*elems):
        for elem in elems:
            node = self.head
            if node.val == elem:
                self.head = node.next
                continue
            prenode = node
            while node.val is not elem:
                prenode = node
                node = node.next
                if node is None:
                    print(f"Node with value {elem} doesn't exist")
                    return
            prenode.next = node.next

    def remove_index(self,index):
        node = self.head
        if index == 0:
            self.head = node.next
            return
        prenode = node
        c = 0
        while index != c:
            prenode = node
            node = node.next
            if node is None:
                print(f"No node at index {index}")
                return
            c+=1
        prenode.next = node.next

    def insert_at_index(self,elem,index):
        if index < 0 or index >= self.get_length():
            print(f'invalid index ({index})')
            return
        if index == 0:
            self.insert_beginning(elem)
            return
        node = self.head
        c = 0
        while index != c:
            prenode = node
            node = node.next
            c+=1
        prenode.next = Node(elem,node)

    def insert_at_value(self,elem,nodeval):
        if self.head.val == nodeval:
            self.insert_beginning(elem)
            return
        node = self.head
        prenode = node
        while node and node.val != nodeval:
            prenode = node
            node = node.next
            if node is None:
                print(f"node with value {nodeval} not found")
        prenode.next = Node(elem,node)




liste = LinkedList()
n1 = Node('hello')
n2 = Node('World')

liste.insert_beginning('space')
liste.insert_beginning('yay')
liste.insert_afternode('ho',liste.head)
liste.insert_end("hahahah")
liste.paste_arr([1,2,3])
liste.insert_at_value('abdoul','hahahah')

liste.print()
print(liste.get_length())

testliste = LinkedList()
testliste.paste_arr([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
testliste.remove_elems(1,2,3,19)

testliste.remove_index(0)
testliste.insert_at_index(100,5)
testliste.insert_at_index(65,0)
testliste.print()
print(testliste.get_length())