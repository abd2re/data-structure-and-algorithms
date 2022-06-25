class TreeNode:
    def __init__(self,value):
        self.value = value
        self.children = []
        self.parent = None

    def add_children(self,*children):
        for child in children:
            child.parent = self
            self.children.append(child)

    def level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level

    def print(self):
        spaces = ' ' * self.level() * 3
        prefix = spaces + '|__' if self.parent else ""

        print(prefix + self.value)

        for child in self.children:
            child.print()


root = TreeNode('Electronics')

computer = TreeNode('computer')
phone = TreeNode('phone')
tv = TreeNode('tv')

root.add_children(computer,phone,tv)

computer.add_children(TreeNode('windows'),TreeNode('Macbook'))
phone.add_children(TreeNode('linux'),TreeNode('iphone'),TreeNode('Android'))
tv.add_children(TreeNode('Samsung'),TreeNode('LG'))


root.print()

