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
        nodeSet = [] #aScore, node
        aScores = {} #node, gScore + distance
        gScores = {} #edge cost
        parents = {} #parent node
        #have hValues in heuristics[]

        gScores[startNode] = 0
        aScores[startNode] = gScores.get(startNode) + heuristics[startNode]

        heappush(nodeSet, (aScores.get(startNode), startNode))

        while len(nodeSet) > 0:

            if goalNode not in self.visited:

                currentAScore, currentNode = heappop(nodeSet)

                if currentNode != goalNode:

                    for neighbor in range(len(matrix)):
                        neighborEdge = matrix[currentNode][neighbor]
                        neighGScore = matrix[currentNode][neighbor] + gScores.get(currentNode)
                        if neighborEdge > 0:

                            if neighbor not in self.visited and neighbor not in aScores:
                                gScores[neighbor] = neighGScore #edge cost to neighbor
                                aScores[neighbor] = gScores.get(neighbor) + heuristics[neighbor]
                                heappush(nodeSet, (aScores[neighbor], neighbor))
                                parents[neighbor] = currentNode
                            else:
                                nAScore = neighGScore + heuristics[neighbor]

                                if nAScore < aScores.get(neighbor):
                                    gScores[neighbor] = neighGScore #edge cost to neighbor
                                    aScores[neighbor] = gScores.get(neighbor) + heuristics[neighbor]
                                    heappush(nodeSet, (aScores[neighbor], neighbor))
                                    parents[neighbor] = currentNode



                    self.visited.append(currentNode)
                else:
                    self.visited.append(currentNode)
                    self.printPath(startNode, goalNode, parents, aScores)
            else:
                return

    @classmethod
    def printPath(self, startNode : int, goalNode : int, parents : dict, aScores: dict):

        path = []
        print("Lowest Cost Path: ", end="")
        current = goalNode
        while current != startNode:
            path.append(current)
            current = parents[current]

        path.append(startNode)

        for node in reversed(path):
            print(f"->{self.vertices.get(node)}({aScores[node]})",end="")

        print()

        

    @classmethod
    def printVisited(self):
        print("Visited Search State: ", end="")
        for node in self.visited:
            print(f"->{self.vertices.get(node)}", end="")