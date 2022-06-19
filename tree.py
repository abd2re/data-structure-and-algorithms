class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,*childrenNode):
        for childNode in childrenNode:
            childNode.parent = self
            self.children.append(childNode)

    def get_generation(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_generation() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()


root = TreeNode('Electronics')

computer = TreeNode('Computer')
phone = TreeNode('Phone')
tv = TreeNode('TV')

root.add_child(computer,phone,tv)

def parenting(parentNode,array):
    [parentNode.add_child(TreeNode(data)) for data in array]

parenting(computer,['Macbook','Windows','Linux'])
parenting(phone,['Iphone','Android'])
parenting(tv,['Samsung','LG'])



root.print_tree()




