from TreeNode import *
"""
124 Binary Tree Maximum Path Sum

Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""
# similar problems: 938 Range Sum of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    maxSum = 0
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.maxSum = root.val
        self._localMax(root)

        return self.maxSum
    
    def _localMax(self, root):
        """
        get the local max of node root
        """
        if not root:
            return 0

        leftMax = self._localMax(root.left)
        rightMax = self._localMax(root.right)
        localMax = max(root.val, root.val + leftMax, root.val + rightMax)   # local max is comparison between root, left branch + root, right branch + root

        self.maxSum = max(localMax, root.val + leftMax + rightMax, self.maxSum) # global max is comparison between local max, left branch + root + right branch, global max

        return localMax

obj = Solution()
test_case = [1, 2, 3, 4]
print(obj.maxPathSum(ListToTree(test_case)))