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
        
        openSet = [] #Priority queue to store nodes to be evaluated
        heappush(openSet, startNode)

        cameFrom = {}
        gScore = {}
        fScore = {}

        #Adding startNode key, values
        gScore[startNode] = 0
        fScore[startNode] = 10
        tentGScore = 0

        while len(openSet) > 0:
            currentNode = heappop(openSet) #Get node will lowest fScore

            if currentNode == goalNode:
                #Do stuff here
                print("Done")
                return
            
            for neighbor in range(len(matrix)):

                edgeCost = matrix[currentNode][neighbor]

                if edgeCost > 0: #Check if there is a neighbor
                    gScore[neighbor] = edgeCost
                    tentGScore = gScore.get(currentNode) + gScore.get(neighbor)  #cost from current node to next node

                    if gScore.get(currentNode) < gScore.get(neighbor):
                        cameFrom[neighbor] = currentNode
                        gScore[neighbor] = tentGScore
                        fScore[neighbor] = gScore[neighbor] + heuristics[neighbor]

                        if neighbor not in openSet:
                            openSet.append(neighbor)


            

