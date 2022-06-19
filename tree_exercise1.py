class TreeNode:
    def __init__(self,name,title):
        self.name = name
        self.title = title
        self.children = []
        self.parent = None

    def add_children(self,child):
        child.parent = self
        self.children.append(child)

    def generation(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def type(self,show):
        if show == 'name':
            return self.name
        if show == 'designation':
            return self.title
        if show == 'both':
            return f'{self.name} ({self.title})'
        else:
            print('Invalid argument')
            return False

    def print(self,show):
        datatype = self.type(show)
        if not datatype:
            return
        spaces = ' ' * self.generation() * 3
        prefix = spaces + '|__' if self.parent else ""

        print(prefix + datatype)
        for child in self.children:
            child.print(show)

    def find_child(self,name,title):
        for child in self.children:
            if name == child.name and title == child.title:
                return child
        for child in self.children:
            return child.find_child(name,title)


root = TreeNode('Nilupul','CEO')

def parenting(parent,arr):
    [parent.add_children(TreeNode(name, title)) for name, title in arr] # arr -> list of tuples

parenting(root,[('Chinmay','CTO'),
                ('Gels','HR Head')])




parenting(root.find_child('Chinmay','CTO'),[('Vishwa','Infrastructure Head'),
                                            ('Aamir','Application Head')])
parenting(root.find_child('Gels','HR Head'),[('Peter','Recruitement Manager'),
                                             ('Waqas','Policy Manager')])
parenting(root.find_child('Vishwa','Infrastructure Head'),[('Dhaval','Cloud Manager'),
                                                           ('Abhijit','App Manager')])

root.print('both')











