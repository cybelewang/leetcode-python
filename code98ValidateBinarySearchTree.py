"""
98 Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
# What's the result if root is None?
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        sysMin = -2**31
        sysMax = 2**31 - 1

        return self._isValid(root, sysMin-1, sysMax + 1)

    def _isValid(self, root, minLimit, maxLimit):
        """
        Compare the root with minLimit and maxLimit; Update these limits when traverse to lower level nodes
        :type root: TreeNode
        :type minLimit: int
        :type maxLimit: int
        """
        res = root.val > minLimit and root.val < maxLimit
        if not res:
            return False
        else:
            if root.left is not None:
                res = res and self._isValid(root.left, minLimit, min(root.val, maxLimit))
            if root.right is not None:
                res = res and self._isValid(root.right, max(minLimit, root.val), maxLimit)
            return res

# 2nd round solution on 9/20/2018
class Solution2:
    def isValidBST(self, root):
        def valid(root, lower, upper):
            if not root:
                return True

            if lower < root.val < upper:
                return valid(root.left, lower, root.val) and valid(root.right, root.val, upper)
            else:
                return False

        return valid(root, -2**31-1, 2**31)

obj = Solution2()
test_cases = [[], [1], [1, 2, 3], [2, 1, 3], [5, 2, 9, 1, 6, 7, 10]] 
for case in test_cases:
    test_tree = ListToTree(case)
    print(obj.isValidBST(test_tree))