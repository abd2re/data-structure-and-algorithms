from collections import deque
from tkinter.tix import Tree

class TreeNode:
    def __init__(self,name,title):
        self.name = name
        self.title = title
        self.children = []
        self.parent = None

    def add_children(self,*children):
        for child in children:
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





root = TreeNode('Nilupul','CEO')
CTO = TreeNode('Chinmay','CTO')
HR_Head = TreeNode('Gels','HR Head')
Infr_Head = TreeNode('Vishwa','Infrastructure Head')
App_Head = TreeNode('Aamir','Application Head')
Recru_Manager = TreeNode('Peter','Recruitement Manager')
Policy_Manager = TreeNode('Waqas','Policy Manager')
Cloud_Manager = TreeNode('Dhaval','Cloud Manager')
App_Manager = TreeNode('Abhijit','App Manager')

root.add_children(CTO,HR_Head)
CTO.add_children(Infr_Head,App_Head)
HR_Head.add_children(Recru_Manager,Policy_Manager)
Infr_Head.add_children(Cloud_Manager,App_Manager)



root.print('both')











