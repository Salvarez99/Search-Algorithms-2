import numpy as np
from heapq import *


class Greedy:

    # Change to priority queue
    visited = []

    vertices = {0: 'A',
                1: 'B',
                2: 'C',
                3: 'D',
                4: 'E',
                5: 'F',
                6: 'G',
                7: 'H',
                8: 'P',
                9: 'Q',
                10: 'R',
                11: 'S'}

    """
    TODO:
        Use a priority queue instead of a list
    """
    @classmethod
    def greedySearch(self, startNode: int, goalNode: int, matrix: np.ndarray, heuristics: list[int]) -> None:

        currentNode = startNode

        # Continue while goal node is not reached
        while currentNode != goalNode:

            self.visited.append(currentNode)

            # Priority Queue
            heuristicValues = []
            # List
            neighbors = []
            """
                Search through all neighbors
                Create a list of neighbors and list of their hValues
            """
            for neighbor in range(len(matrix)):
                if neighbor not in self.visited and matrix[currentNode][neighbor] > 0:
                    hValue = heuristics[neighbor]
                    heappush(heuristicValues, hValue)
                    neighbors.append(neighbor)

            """
            PQ will give me the lowest hValue
            Need to find the node correlated to that hValue
            Then set currentNode equal to correlated node
            """
            nextHValue = heappop(heuristicValues)
            for neighbor in neighbors:
                if heuristics[neighbor] == nextHValue:
                    currentNode = neighbor

        self.visited.append(currentNode)

    @classmethod
    def printVisited(self):
        for node in self.visited:
            print(f"->{self.vertices.get(node)}", end="")
