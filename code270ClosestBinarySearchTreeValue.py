"""
270 Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""
from TreeNode import *
class Solution:
    def closestValue(root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        

lt = []
lt = [1]
lt = [1, None, 2]
lt = [1, 2, None, 3, None, 4, None]
lt = [5, 2, 13]
root = ListToTree(lt)
PrintTree(root)
PrintTree(Solution().convertBST(root))