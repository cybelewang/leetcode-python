from TreeNode import *
"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        if not root:
            return res

        level = [root]
        while len(level) > 0:
            newLevel = []
            siblings = []
            for node in level:
                siblings.append(node.val)
                if node.left is not None:
                    newLevel.append(node.left)
                if node.right is not None:
                    newLevel.append(node.right)
            
            res.append(siblings)
            level = newLevel
        
        res.reverse()
        
        return res

obj = Solution()
null = None
test_case = [3,9,20,null,null,15,7]
test_tree = ListToTree(test_case)
print(obj.levelOrderBottom(test_tree))