class Minimax:
    index = 0

    def __init__(self, value=None, index=None):
        if index is None:
            self.index = Minimax.index
            Minimax.index += 1
        else:
            self.index = index

        self.value = value
        self.left = None
        self.right = None

    @classmethod
    def buildTree(self, depth, max_turn, values, index=None):
        if depth == 0:
            return Minimax(values.pop(0), index)

        root = Minimax(index=index)

        if max_turn:
            root.left = self.buildTree(
                depth - 1, False, values, index=root.index + 1)
            root.right = self.buildTree(
                depth - 1, False, values, index=root.index + 1)
        else:
            root.left = self.buildTree(
                depth - 1, True, values, index=root.index + 1)
            root.right = self.buildTree(
                depth - 1, True, values, index=root.index + 1)

        return root

    @classmethod
    def minimax(self, node, depth, max_turn):
        if depth == 0 or node is None:
            return node.value

        if max_turn:
            return max(self.minimax(node.left, depth - 1, False), self.minimax(node.right, depth - 1, False))
        else:
            return min(self.minimax(node.left, depth - 1, True), self.minimax(node.right, depth - 1, True))

    @classmethod
    def minimaxABPrune(self, node, depth, max_turn, alpha=float('-inf'), beta=float('inf')):
        if depth == 0 or node is None:
            return node.value, node

        best_state = None

        if max_turn:
            value = float('-inf')
            for child in [node.left, node.right]:
                if child is not None:
                    child_value, _ = self.minimaxABPrune(child, depth - 1, False, alpha, beta)
                    if child_value > value:
                        value = child_value
                        best_state = child
                    alpha = max(alpha, value)
                    if alpha >= beta:
                        break
            return value, best_state
        else:
            value = float('inf')
            for child in [node.left, node.right]:
                if child is not None:
                    child_value, _ = self.minimaxABPrune(child, depth - 1, True, alpha, beta)
                    if child_value < value:
                        value = child_value
                        best_state = child
                    beta = min(beta, value)
                    if alpha >= beta:
                        break
            return value, best_state

    @classmethod
    def getOptimalStateMini(self, values):
        root = self.buildTree(4, True, values)
        optimal_value = self.minimax(root, 4, True)
        return root, optimal_value


    @classmethod
    def getOptimalStateMiniAB(self, values):
        root = self.buildTree(4, True, values)
        optimal_value, optimal_state = self.minimaxABPrune(root, 4, True)
        return optimal_state, optimal_value

    @classmethod
    def printTree(self, root, level=0, node="Root: "):
        if root is not None:
            print(" " * (level * 4) + node + f"({root.index}): {root.value}")

            if root.left != None or root.right != None:
                self.printTree(root.left, level + 1, f"L{root.left.index}--- ")
                self.printTree(root.right, level + 1, f"R{root.left.index}--- ")
