from TreeNode import *
"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        build, res = [], []

        self._recursive(root, sum, build, res)

        return res

    def _recursive(self, root, sum, build, res):
        
        if not root:
            return
        
        build.append(root.val)
        if root.left is None and root.right is None and root.val == sum:
            res.append(build[:])
            build.pop()
            return

        if root.left is not None:
            self._recursive(root.left, sum - root.val, build, res)
        
        if root.right is not None:
            self._recursive(root.right, sum - root.val, build, res)

        build.pop()

obj = Solution()
null = None
test_case = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]
test_tree = ListToTree(test_case)
print(obj.pathSum(test_tree, 22))          
