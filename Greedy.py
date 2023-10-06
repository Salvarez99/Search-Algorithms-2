import numpy as np

class Greedy:

    #Change to priority queue
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

    def greedySearch(self, startNode: int, goalNode : int, matrix: np.ndarray, heuristics : dict[str, int]) -> None:

        self.visited.append(startNode)
        currentNode = startNode

        while currentNode != goalNode:

            heuristicValues = {}

            for neighbor in len(matrix):
    
                neighborEdgeCost = matrix[currentNode][neighbor] 
                
                if neighborEdgeCost > 0:
    
                    neighborNodeLetter = self.vertices.get(neighbor)
                    neighborHeuristic = heuristics.get(neighborNodeLetter)
                    heuristicValues.append(neighborNodeLetter, neighborHeuristic)

            minVal = 10000
            nextNodeLetter = ""

            for letter , value in heuristicValues:
                if minVal < value:
                    minVal = value
                    nextNodeLetter = letter

            currentNode = 


     






        return

