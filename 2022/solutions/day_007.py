from utils import *


class Node:
    def __init__(self, name, parent=None, size=0):
        self.name: str = name
        self.parent = parent  # type of Node
        self.children: list[Node] = []
        self.size: int = size

    def __repr__(self):
        return self.name

    def get_value(self):
        return self.size

    def get_children(self):
        return self.children

    def add_value(self, value):
        self.size += value

    def create_and_enter_dir(self, name_input):
        node1 = Node(name=name_input)
        self.children.append(node1)
        node1.parent = self
        return node1

    def exit_directory(self):
        return self.parent

    def enter_directory(self, name):
        for dirs in self.children:
            if dirs.name == name:
                return dirs

    def return_to_root(self):
        while self.parent != None:
            self = self.exit_directory()
        return self

    def update_sizes(self):
        for subdir in self.children:
            self.size += self.update_size_subdir(subdir)

    def update_size_subdir(self, node):
        for subdir in node.children:
            node.size += self.update_size_subdir(subdir)
        return node.size


    def sum(self, max):
        total = 0
        if len(self.children) != 0: # children exist 
            for subdir in self.children:
                total += sum(subdir, max)
                print(subdir)
                print(dir)
        else:  # no children 
            for dir in self.children:
                if dir.size <= max:
                    total += dir.size
                    print(dir)
                    print(total)
                    print("pass")
        return total


    # def jacob_sum_outer(self):
    #     total = 0
    #     total = self.jacob_sum_recursive(self, total)
    #     return(total)


    def jacob_sum_recursive(self):
        total = 0 
        if self.size <= 100000:
            total += self.size
        for dir in self.children:
            total += dir.jacob_sum_recursive()
        return(total)
        
        
# 95437

    # def sum_dirs(self, max):
    #     for subdir in self.children:
    #         self.total += self.sum_subdirs(subdir, max)
    #         print(subdir)
    #     return(self.total)

    # def sum_subdirs(self, node, max):
    #     for subdir in node.children:
    #         print(subdir)
    #         if subdir.size <= max:
    #             return(self.size)
    #             print('pass')
    #         else:
    #             return(0)
    #     #return(sum)

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other: int):
        return self.size <= other

    def __ge__(self, other: int):
        return self.size >= other

    def __add__(self, other: int):
        return self.size + other

    def __radd__(self, other: int):
        return self.size + other


# def add_data(self, )
def extract_file_structure(data):
    Tree = Node("/")
    for line in data:
        if ("$ cd" in line) and (line != "$ cd /"):
            if line[5:] == "..":
                # revert to previous directory up ('go_up')
                print(line)
                Tree = Tree.exit_directory()
                print(Tree)
            else:
                # Create new sub directory with line[4:] as name ('add_node' w/ name)
                print(line)
                Tree = Tree.create_and_enter_dir(name_input=line[5:])
        elif ("dir" in line) or ("$ ls" in line):
            pass
        elif contains_number(line):
            # add to current directory data
            print(line)
            # print(int(re.findall(r"\d+", 'abc123')[0]))
            Tree.add_value(int(re.findall(r"\d+", line)[0]))
            print(Tree.get_value())
        else:
            print("Read error")
            print(line)
    Tree = Tree.return_to_root()
    print(Tree)
    print(Tree.get_children())
    print(Tree.update_sizes())
    Tree = Tree.return_to_root()
    # Tree = Tree.enter_directory('a')
    # print(Tree.get_value())
    # print(Tree)
    # print(Tree.get_children())
    # print(sum(filter(lambda x: x <= 100000, Tree.children)))
    # print(Tree.sum_dirs(100000))
    print(Tree.jacob_sum_recursive())



## TEST
test = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]

extract_file_structure(test)

extract_file_structure(Input("007").read().splitlines())

# print(Input("007").read().splitlines())


