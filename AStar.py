import numpy as np
from heapq import *


class AStar:

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

    @classmethod
    def aStarSearch(self, startNode: int, goalNode: int, matrix: np.ndarray, heuristics: list[int]) -> None:
        """
        Greedy
        Look through neighbors
        Find lowest hValue
        Set currentNode to node with lowest hValue

        UCS


        """

        priority_queue = []

        currentNode = startNode

        # Push startnode into priority queue
        # (edgecost, node)

        while len(priority_queue) > 0:

            heappush(priority_queue, (0, currentNode))
            currentEdgeCost, currentNode = heappop(priority_queue)

            self.visited.append(currentNode)

            # Priority Queue
            heuristicValues = []
            # List
            neighbors = []

            if currentNode == goalNode:
                return

            # Traverse through neighboring nodes
            for neighbor in range(len(matrix)):

                # If there is a neighboring node
                if currentNode not in self.visited and matrix[currentNode][neighbor] > 0:

                    """list neighbors and place hValues in heap"""
                    hValue = heuristics[neighbor]
                    heappush(heuristicValues, hValue)
                    neighbors.append(neighbor)

                    # Store edge cost
                    neighborEdgeCost = matrix[currentNode][neighbor]

                    totalCost = currentEdgeCost + neighborEdgeCost

                    if currentNode not in self.visited:
                        # Check if neighboring node has been visited OR if current path is shorter
                        if neighbor not in self.visited or totalCost < neighborEdgeCost:

                            # Update edge cost of neighboring node
                            matrix[currentNode][neighbor] = totalCost

                            # Push total cost and current neighboring node
                            heappush(priority_queue, (totalCost, neighbor))

                nextHValue = heappop(heuristicValues)

                if heuristics[currentNode] > nextHValue:

                    for neighbor in neighbors:
                        if heuristics[neighbor] == nextHValue:
                            currentNode = neighbor

        return
