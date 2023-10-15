import numpy as np
from Greedy import *
from AStar import *
from Minimax import *


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
graph_heuristics = [5, 7, 4, 7, 5, 2, 0, 11, 14, 12, 3, 10]

# leaf nodes for minimax
values = [3, 10, 2, 9, 10, 7, 5, 9, 2, 5, 6, 4, 2, 7, 9, 1]


print("Greedy Search")
Greedy.greedySearch(11, 6, np_matrix, graph_heuristics)
Greedy.printVisited()

print("\n\nA* Search")
AStar.aStarSearch(11, 6, np_matrix, graph_heuristics)
AStar.printVisited()

print("\n\nMinimax:")
optimal_state, optimal_value = Minimax.getOptimalStateMini(values)
print("Tree Structure:")
Minimax.printTree(optimal_state)
print("\nOptimal Move Value:", optimal_value)

print("\n\nMinimax alpha beta pruning:")
values = [3, 10, 2, 9, 10, 7, 5, 9, 2, 5, 6, 4, 2, 7, 9, 1]
optimal_state, optimal_value = Minimax.getOptimalStateMiniAB(values)
print("Tree Structure:")
Minimax.printTree(optimal_state)
print("\nOptimal Move Value:", optimal_value)