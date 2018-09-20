"""
104 Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
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
        if not root:
            return 0

        parents = [root]
        level = 0

        while len(parents) > 0:
            children = []
            for parent in parents:
                if parent.left is not None:
                    children.append(parent.left)
                if parent.right is not None:
                    children.append(parent.right)
            parents = children
            level += 1
        
        return level

null = None
test_case = [1,null, 2, null, 3]
obj = Solution()
test_tree = ListToTree(test_case)
print(obj.maxDepth2(test_tree))