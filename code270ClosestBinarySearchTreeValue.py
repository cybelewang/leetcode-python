"""
270 Closest Binary Search Tree Value    -   not submitted

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""
from TreeNode import *
class Solution:
    # iterative solution
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = float('inf')
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val

            if root.val < target:
                root = root.right
            else:
                root = root.left

        return res
    
    # recursive solution
    def closestValue_dfs(self, root, target):
        self.res = float('inf')
        def dfs(node):
            if not node:
                return
            if abs(node.val - target) < abs(self.res - target):
                self.res = node.val
            
            if node.val < target:
                dfs(node.right)
            else:
                dfs(node.left)

        # main
        dfs(root)
        return self.res

lt, target = [1], 1.3
lt, target = [5, 3, 7, 2, 4, 6, 8], 6.49
root = ListToTree(lt)
PrintTree(root)
print(Solution().closestValue_dfs(root, target))