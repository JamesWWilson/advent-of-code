from utils import *
from queue import Queue
import string
import copy

input_test = Input("012_test").read().splitlines()
# input = Input("012").read().splitlines()

print(input_test)

## first transform all letters into numbers
def content_dict():
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    contents = {}
    letters = string.ascii_lowercase + string.ascii_uppercase
    for i in range(1, 53):  # needs to be 1-53 to capture 'Z'
        contents[letters[i - 1]] = i
    return contents


## Create terrain
def create_terrain(key):
    terrain = []
    for line in input_test:
        line_values = []
        for char in line:
            if char == "S":
                value = 1
            elif char == "E":
                value = 27  # one more than z aka 26
            else:
                value = key.get(char)
            line_values.append(value)
        terrain.append(copy.deepcopy(line_values))
    return terrain


terrain = create_terrain(content_dict())

# 0,0 = node 0 
# 0,1 = node 1 
# 1,0 = node len(terrain) 
# 1,1 = node len(terrain) + 1 
# 


class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)

        # Directed or Undirected
        self.m_directed = directed

        # Graph representation - Adjacency list
        # We use a dictionary to implement an adjacency list
        self.m_adj_list = {node: set() for node in self.m_nodes}

    # Add edge to the graph
    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))

        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))

    # Print the graph representation
    def print_adj_list(self):
      for key in self.m_adj_list.keys():
        print("node", key, ": ", self.m_adj_list[key])



graph = Graph(3, directed=False)
graph.add_edge("10", "20")
graph.add_edge("10", "30")
graph.add_edge("01", "30")

graph.print_adj_list()


## Create graph
# for i in range(0,len(terrain)):
#     for j in range(0,len(terrain[0])):
#         terrain[i][j]
#         print(i,j)
#         # new - current <= 1:
#         if (i + 1) < len(terrain):
#             if terrain[i+1][j] - terrain[i][j] <= 1:
#                 print("append", terrain[i+1][j], "to", terrain[i][j])
#         if (i - 1) > 0:
#             if terrain[i-1][j] - terrain[i][j] <= 1:
#                 print("append", terrain[i-1][j], "to", terrain[i][j])
#         if (j + 1) < len(terrain[0]):
#             if terrain[i][j+1] - terrain[i][j] <= 1:
#                 print("append", terrain[i][j+1], "to", terrain[i][j])
#         if (j - 1) > 0:
#             if terrain[i][j-1] - terrain[i][j] <= 1:
#                 print("append", terrain[i][j-1], "to", terrain[i][j])


# check each adjacent node.
# needs to not be higher than 1 and exist to append

# else ignore
