import numpy as np
from BinaryTree import *
from Greedy import *

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

# Indicates an estimate of how close the current state is to the goal
"""h(S) = 10"""
#                   A  B  C  D  E  F  G  H  P  Q  R  S
graph_heuristics = [5, 7, 4, 7, 5, 2, 0, 11,14,12,3, 10]

Greedy.greedySearch(11, 6, np_matrix, graph_heuristics)
Greedy.printVisited()

# BinaryTree.testTree()