from TreeNode import *
"""
110 Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        res = self._depth(root)

        return res[1]
        
    def _depth(self, root):
        """
        return (max depth, is balanced)
        """
        if not root:
            return (0, True)
        
        (leftDepth, leftBalanced) = self._depth(root.left)
        (rightDepth, rightBalanced) = self._depth(root. right)

        return (1 + max(leftDepth, rightDepth), leftBalanced and rightBalanced and (-2 < (leftDepth - rightDepth) < 2))

    # 2nd round solution on 11/26/2018
    def isBalanced2(self, root):
        def maxdepth(node):
            """
            get max depth of the subtree with node as the root
            return -1 if two subtrees have depth difference > 1
            """
            if not node:
                return 0
            
            leftdepth, rightdepth = maxdepth(node.left), maxdepth(node.right)
            if leftdepth == -1 or rightdepth == -1 or abs(leftdepth - rightdepth) > 1:
                return -1
            else:
                return 1 + max(leftdepth, rightdepth)
        
        return maxdepth(root) > -1

obj = Solution()
null = None
test_case = [1, 2]
test_tree = ListToTree(test_case)
print(obj.isBalanced2(test_tree))        