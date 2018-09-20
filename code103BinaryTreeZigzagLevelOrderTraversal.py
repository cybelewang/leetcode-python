"""
103 Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        level = [root]
        reverse = False
        while len(level) > 0:
            levelRes = []
            newLevel = []
            for node in level:
                levelRes.append(node.val)
                if node.left is not None:
                    newLevel.append(node.left)
                if node.right is not None:
                    newLevel.append(node.right)
            if reverse:
                levelRes.reverse()
            res.append(levelRes)
            level = newLevel
            reverse = not reverse

        return res

null = None
test_case = [3,9,20,null,null,15,7]
obj = Solution()
test_tree = ListToTree(test_case)
print(obj.zigzagLevelOrder(test_tree))