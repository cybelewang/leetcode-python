from TreeNode import *
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive solution
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # iterative solution, using level order traversal
    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        

null = None
test_case = [1,2,3]
obj = Solution()
test_tree = ListToTree(test_case)
print(obj.maxDepth(test_tree))