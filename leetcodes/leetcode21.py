from typing import List


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def print(self):
        node = self
        while node:
            print(node.val)
            node = node.next

l1 = ListNode(1,ListNode(2,ListNode(4,ListNode(5))))
l2 = ListNode(1,ListNode(3,ListNode(4)))

#l1.print()
#l2.print()

def mergeTwoLists(l1,l2):
    mergedlist = ListNode()
    head = mergedlist

    while l1 and l2:
        if l1.val < l2.val:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next

    if l1:
        head.next = l1
    elif l2:
        head.next = l2


    mergedlist.next.print()

mergeTwoLists(l1,l2)