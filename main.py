import numpy as np
from BinaryTree import *
import sys
sys.path.insert(
    0, "c:\\Users\\xenep\\OneDrive\\Documents\\UAlbany\\Fall 2023\\ICSI 435 AI\\Alvarez_S_Homework1")
from convert import *

np_matrix = np.array([(0,  2,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0),
                      (2,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0),
                      (2,  0,  0,  8,  0,  3,  0,  0,  0,  0,  0,  0),
                      (0,  1,  8,  0,  2,  0,  0,  0,  0,  0,  0,  3),
                      (0,  0,  0,  2,  0,  0,  0,  8,  0,  0,  2,  9),
                      (0,  0,  3,  0,  0,  0,  2,  0,  0,  0,  2,  0),
                      (0,  0,  0,  0,  0,  2,  0,  0,  0,  0,  0,  0),
                      (0,  0,  0,  0,  8,  0,  0,  0,  4,  4,  0,  0),
                      (0,  0,  0,  0,  0,  0,  0,  4,  0,  15, 0,  1),
                      (0,  0,  0,  0,  0,  0,  0,  4,  15, 0,  0,  0),
                      (0,  0,  0,  0,  2,  2,  0,  0,  0,  0,  0,  0),
                      (0,  0,  0,  3,  9,  0,  0,  0,  1,  0,  0,  0)])

# indicates an estimate of how close the current state is to the goal
graph_heuristics = {'S': 0,
                    'A': 5,
                    'B': 7,
                    'C': 4,
                    'D': 7,
                    'E': 5,
                    'F': 2,
                    'H': 11,
                    'P': 14,
                    'Q': 12,
                    'R': 3,
                    'G': 0}

# matrix = np.zeros((12,12), dtype=int)

# vertex_list = {'S': ['D', 'E', 'P'],
#                'A': ['B', 'C'],
#                'B': ['A', 'D'],
#                'C': ['A', 'D', 'F'],
#                'D': ['B', 'C', 'E', 'S'],
#                'E': ['D', 'H', 'R', 'S'],
#                'F': ['C', 'G', 'R'],
#                'H': ['E', 'P', 'Q'],
#                'P': ['H', 'Q', 'S'],
#                'Q': ['H', 'P'],
#                'R': ['E', 'F'],
#                'G': ['F']}

# edge_list = {'S': [3, 9, 1],
#              'A': [2, 2],
#              'B': [2, 1],
#              'C': [2, 8, 3],
#              'D': [1, 8, 2, 3],
#              'E': [2, 8, 2, 9],
#              'F': [3, 2, 2],
#              'H': [8, 4, 4],
#              'P': [4, 15, 1],
#              'Q': [4, 15],
#              'R': [2, 2],
#              'G': [2]}

# matrix = convert.convertListToMatrixW(matrix, vertex_list, edge_list)
# convert.printAdjMatrix(matrix)

BinaryTree.testTree()
