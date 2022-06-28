class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def in_order_traversal(self):
        elements = []
        #left
        if self.left:
            elements += self.left.in_order_traversal()
        #root node
        elements.append(self.data)
        #right
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False


    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if self == None:
            return self
        if val == self.data:
            if self.left is None:
                self = self.right
            elif self.right is None:
                self = self.left
            else:
                temp = self.left.find_max()
                self.delete(temp)
                self.data = temp
        elif val < self.data:
            self.left = self.left.delete(val)
        else:
            self.right = self.right.delete(val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


numbers = [17,4,1,20,9,23,18,34]
numbers_tree = build_tree(numbers)

print(numbers_tree.in_order_traversal())
numbers_tree.delete(20)
print(numbers_tree.in_order_traversal())

