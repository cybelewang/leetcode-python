"""

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    # my own solution, modified inorder traversal
    # need to consider 
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 2**32 - 1
        def inorder(root, prev):
            if root:
                prev = inorder(root.left, prev)
                self.res = min(self.res, root.val - prev)
                prev = inorder(root.right, root.val)
            
            return prev
        
        inorder(root, -2**31)

        return self.res

root = ListToTree([9, 6, 19, None, 8])
PrintTree(root)
print(Solution().getMinimumDifference(root)) 