"""
513 Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    # recursive solution
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = root.val
        self.h = 0
        def dfs(node, h):
            if node.left is None:
                if h > self.h:
                    self.res = node.val
                    self.h = h
            else:
                dfs(node.left, h+1)

            if node.right is not None:
                dfs(node.right, h+1)
        
        # main
        dfs(root, 0)

        return self.res

#root = ListToTree([1])
root = ListToTree([1, 2, 3, 4, None, 5, 6, None, None, 7])
PrintTree(root)
print(Solution().findBottomLeftValue(root))