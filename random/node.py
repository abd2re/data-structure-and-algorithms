class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def readLinkedList(self):
        node = self.head
        while node is not None:
            print(node.val)
            node = node.next

    def insertBeginning(self,newval):
        newnode = Node(newval)
        newnode.next = self.head
        self.head = newnode

    def insertEnd(self,newval):
        newnode = Node(newval)
        if self.head is None:
            self.head = newnode
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = newnode

    def insertAfter(self,afterNode,newval):
        if afterNode is None:
            print("node doesn't exist")
            return
        else:
            newnode = Node(newval)
            newnode.next = afterNode.next
            afterNode.next = newnode


names = ['lundi','mardi','mercredi','jeudi']
nodes = list(map(lambda x: Node(x), names))
liste = LinkedList()

for i in range(len(nodes)):
    if i == 0:
        liste.head = nodes[i]
    else:
        nodes[i-1].next = nodes[i]


liste.insertBeginning('dimanche')
liste.insertEnd('vendredi')
liste.insertEnd('samedi')
liste.insertAfter(nodes[3].next,'works')
liste.readLinkedList()

print(nodes)