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

    def inOrderTraversal(self):
        arr = []

        if self.left:
            arr += self.left.inOrderTraversal()

        arr.append(self.data)

        if self.right:
            arr += self.right.inOrderTraversal()

        return arr

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def calculate_sum(self):
        returnSum = self.data
        if self.left:
            returnSum += self.left.calculate_sum()
        if self.right:
            returnSum += self.right.calculate_sum()

        return returnSum

    def preOrderTraversal(self):
        arr = []
        arr.append(self.data)
        if self.left:
            arr += self.left.preOrderTraversal()
        if self.right:
            arr += self.right.preOrderTraversal()

        return arr

    def postOrderTraversal(self):
        arr = []
        if self.left:
            arr += self.left.postOrderTraversal()
        if self.right:
            arr += self.right.postOrderTraversal()
        arr.append(self.data)

        return arr

    def search(self,val):
        if val == self.data:
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


def buildTree(list):
    root = BinarySearchTreeNode(list[0])
    for i in range(1,len(list)):
        root.add_child(list[i])
    return root

tree = buildTree([15,12,14,7,27,20,88,23])

print(tree.inOrderTraversal())
print(tree.find_max())
print(tree.find_min())
print(tree.calculate_sum())
print(tree.preOrderTraversal())
print(tree.postOrderTraversal())
print(tree.search(27))
