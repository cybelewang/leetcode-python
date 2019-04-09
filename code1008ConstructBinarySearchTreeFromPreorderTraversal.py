"""
1008 Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.
(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    # https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/252232/JavaC%2B%2BPython-O(N)-Solution
    # O(N) solution
    self.i = 0
    def bstFromPreorder(self, A, bound=float('inf')):
        if self.i == len(A) or A[self.i] > bound:
            return None
        root = TreeNode(A[self.i])
        self.i += 1
        root.left = self.bstFromPreorder(A, root.val)
        root.right = self.bstFromPreorder(A, bound)
        return root
    # my own solution (O(N^2))
    def bstFromPreorder(self, preorder):
        """
        :type preorder: list[int]
        :rtype: TreeNode
        """
        def dfs(preorder, start, end):
            if start > end:
                return None
            root = TreeNode(preorder[start])
            i = start + 1
            while i <= end and preorder[i] < preorder[start]:
                i += 1
            root.left = dfs(preorder, start+1, i-1)
            root.right = dfs(preorder, i, end)

            return root

        # main
        return dfs(preorder, 0, len(preorder) - 1)