class TreeNode:
    def __init__(self,location):
        self.location = location
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

    def print(self,depth):
        space = ' ' * self.generation() * 3
        prefix = space + '|__' if self.parent else ""


        print(prefix + self.location)

        for child in self.children:
            if self.generation() >= depth:
                break
            child.print(depth)


root = TreeNode('Global')
India = TreeNode('India')
USA = TreeNode('USA')
root.add_children(India,USA)

Gujarat = TreeNode('Gujarat')
Karnataka = TreeNode('Karnataka')
India.add_children(Gujarat,Karnataka)

New_Jersey = TreeNode('New Jersey')
California = TreeNode('California')
USA.add_children(New_Jersey,California)

Ahmedbad = TreeNode('Ahmedbad')
Baroda = TreeNode('Baroda')
Gujarat.add_children(Ahmedbad,Baroda)

Bangluru = TreeNode('Bangluru')
Mysore = TreeNode('Mysore')
Karnataka.add_children(Bangluru,Mysore)

Princeton = TreeNode('Princeton')
Trenton = TreeNode('Trenton')
New_Jersey.add_children(Princeton,Trenton)

San_Francisco = TreeNode('San Francisco')
Mountain_View = TreeNode('Mountain View')
Palo_Alto = TreeNode('Palo Alto')
California.add_children(San_Francisco,Mountain_View,Palo_Alto)


root.print(2)



