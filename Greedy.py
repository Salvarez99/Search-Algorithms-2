import numpy as np


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
        # self.visited.append(currentNode)

        # Continue while goal node is not reached
        while currentNode != goalNode:

            self.visited.append(currentNode)

            heuristicValues = []
            neighbors = []
            """
                Search through all neighbors
                Create a list of neighbors and list of their hValues
            """
            for neighbor in range(len(matrix)):
                if neighbor not in self.visited and matrix[currentNode][neighbor] > 0:
                    hValue = heuristics[neighbor]
                    heuristicValues.append(hValue)
                    neighbors.append(neighbor)

            """
                Set current hValue as min
                Iterate through hValues
                Compare current hValue to neighboring hValues
                Find min hValue
                Use min's index to find the node we want to go to
                Set currentNode equal to lowest hValue node
            """
            min = heuristics[currentNode]
            node = -1
            for i in range(len(heuristicValues)):
                if heuristicValues[i] < min:
                    min = heuristicValues[i]
                    node = neighbors[i]

            currentNode = node

        self.visited.append(currentNode)

    @classmethod
    def printVisited(self):
        for node in self.visited:
            print(f"->{self.vertices.get(node)}", end="")
