# You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,
#
# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.
#
# The test cases will be generated such that the binary tree is valid.
from typing import List
from TreeNode import TreeNode

class CreateABinaryTreeFromDescription:
    def buildTree(self,description : List[List[int]]):
        nodes = {}
        childSet = set()

        for node,child,left in description:
            childSet.add(child)

            if node not in nodes:
                nodes[node] = TreeNode(node)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            if left:
                nodes[node].left = nodes[child]
            else:
                nodes[node].right = nodes[child]

        for parent,child,left in description:
            if parent not in childSet:
                return nodes[parent]






classObj = CreateABinaryTreeFromDescription()
print(classObj.buildTree())