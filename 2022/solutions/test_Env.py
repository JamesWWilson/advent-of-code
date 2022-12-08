from utils import *

class Node():
    def __init__(self, name, parent = None, size=0):
        self.name: str = name
        self.parent = parent # type of Node
        self.children: list[Node] = []
        self.size: int = size

    def __repr__(self):
        return self.name

    def get_value(self):
        return self.size

    def add_value(self, value):
        self.size += value 

    def create_and_enter_dir(self, name_input):
        node1=Node(name = name_input)
        self.children.append(node1)
        node1.parent=self
        return node1

    def exit_directory(self):
        return self.parent
    
    def return_to_root(self):
        while self.parent != None:
            self = self.exit_directory()
        return(self)





slash = Node('/')
print(slash)
print(slash.get_value())
slash.add_value(584)

slash = slash.create_and_enter_dir('a')
slash.add_value(29116)
slash = slash.create_and_enter_dir('b')
slash.add_value(888888)

#slash = slash.exit_directory()
slash = slash.return_to_root()
print(slash)
print(slash.get_value())


print('$ cd /'[5])