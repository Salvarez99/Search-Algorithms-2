from typing import Type
import BinaryTree

class BinaryTree:
    left: Type[BinaryTree]
    right: Type[BinaryTree]
    rootid: int
    value: int

    def __init__(self, rootid, value):
        self.left = None
        self.right = None
        self.rootid = rootid
        self.value = value

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNodeValue(self, value):
        self.value = value

    def getNodeValue(self):
        return self.value

    def insertRight(self, newNode, value):
        if self.right == None:
            self.right = BinaryTree(newNode, value)
            # self.right.setNodeValue(value)

        else:
            tree = BinaryTree(newNode, value)
            tree.right = self.right
            self.right = tree

    def insertLeft(self, newNode, value):
        if self.left == None:
            self.left = BinaryTree(newNode, value)
            # self.left.setNodeValue(value)
        else:
            tree = BinaryTree(newNode, value)
            tree.left = self.left
            self.left = tree

    def printTree(self, tree : BinaryTree):
        if tree != None:
            self.printTree(self,tree.getLeftChild())
            print(tree.getNodeValue())
            self.printTree(self,tree.getRightChild())

    @classmethod
    def testTree(self):
        myTree = BinaryTree(1, 0)
        myTree.insertLeft(1, 10)
        myTree.insertRight(1, 11)

        l10 = myTree.getLeftChild()
        l10.insertLeft(1, 20)
        l10.insertRight(1, 21)
        l11 = myTree.getRightChild()
        l11.insertLeft(1, 22)
        l11.insertRight(1, 23)

        self.printTree(self, myTree)
