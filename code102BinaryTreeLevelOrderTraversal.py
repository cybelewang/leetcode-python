"""
102 Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res

        level = [root]
        while len(level) > 0:
            size = len(level)
            levelRes = []
            for i in range(size):
                node = level[i]
                levelRes.append(node.val)
                if node.left is not None:
                    level.append(node.left)
                if node.right is not None:
                    level.append(node.right)
            
            res.append(levelRes)
            level = level[size:]
        
        return res

null = None
test_case = [3,9,20,null,null,15,7]
obj = Solution()
test_tree = ListToTree(test_case)
print(obj.levelOrder(test_tree))