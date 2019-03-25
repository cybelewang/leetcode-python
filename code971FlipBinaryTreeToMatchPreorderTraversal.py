"""
971 Flip Binary Tree To Match Preorder Traversal

Given a binary tree with N nodes, each node has a different value from {1, ..., N}.
A node in this binary tree can be flipped by swapping the left child and the right child of that node.
Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.
(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)
Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.
If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.
If we cannot do so, then return the list [-1].

Example 1:
Input: root = [1,2], voyage = [2,1]
Output: [-1]

Example 2:
Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]

Example 3:
Input: root = [1,2,3], voyage = [1,2,3]
Output: []
 
Note:
1 <= N <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    # https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/solution/
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: list[int]
        :rtype: list[int]
        """        
        self.flip = []
        self.it = 0
        def dfs(node):
            if node:
                if node.val != voyage[self.it]:
                    self.flip = [-1]
                    return
                self.it += 1

                if (self.it < len(voyage)) and node.left and node.left.val != voyage[self.it]:
                    self.flip.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)
            
        #main
        dfs(root)
        if self.flip and self.flip[0] == -1:
            self.flip = [-1]

        return self.flip

root = ListToTree([1, 2, 3, 4, 5, 6, 7])
voyage = [1, 4, 2, 5, 6, 3, 7]
print(Solution().flipMatchVoyage(root, voyage))