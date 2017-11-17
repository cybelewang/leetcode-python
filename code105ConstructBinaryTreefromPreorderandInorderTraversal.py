from TreeNode import *
"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        recursive solution, first look for the index of the first element of preorder in inorder, 
        then dynamically split the preorder and inorder list to left branch and right branch.
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : mid + 1], inorder[ : mid])  # left branch, note the index range
        root.right = self.buildTree(preorder[mid + 1: ], inorder[mid + 1 : ]) # right branch, note the index range

        return root

obj = Solution()
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
res = obj.buildTree(preorder, inorder)
PrintTree(res)