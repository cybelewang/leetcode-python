"""
538 Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    # my own solution, modified reverse-order traversal
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def rev_order(root, prev):
            if root is not None:
                prev = rev_order(root.right, prev)
                root.val += prev
                prev = rev_order(root.left, root.val)

            return prev

        # main
        rev_order(root, 0)

        return root

root = ListToTree([6, 4, 15, None, None, 8, None, 7, 9])
PrintTree(root)
root = Solution().convertBST(root)
PrintTree(root)