"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    def isLeaf(self, node):
        """
        check if node is leaf
        """
        return node is not None and node.left is None and node.right is None

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        res = 0
        if self.isLeaf(root.left):
            res += root.left.val
        else:
            res += self.sumOfLeftLeaves(root.left)
        
        res += self.sumOfLeftLeaves(root.right)

        return res

test_tree = ListToTree([1, 2, 3, 4, 5, 6, 7])
PrintTree(test_tree)
print(Solution().sumOfLeftLeaves(test_tree))