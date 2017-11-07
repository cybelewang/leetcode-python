from TreeNode import *
"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self._generateSubTrees(1, n)

    def _generateSubTrees(self, s, e):
        if s > e:
            return [None]   # bug fixed: should not return [] because this will cause the below for loops not iterate

        res = []
        for i in range(s, e + 1):
            leftSubTrees = self._generateSubTrees(s, i - 1)
            rightSubTrees = self._generateSubTrees(i + 1, e)
            for left in leftSubTrees:
                for right in rightSubTrees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right

                    res.append(root)
        
        return res

obj = Solution()
res = obj.generateTrees(3)
for root in res:
    PrintTree(root)