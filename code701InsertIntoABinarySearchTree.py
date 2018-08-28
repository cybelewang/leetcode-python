"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. 
Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4
"""
# similar problems: 230 Kth Smallest Element in a BST; 315 Count of Smaller Numbers after Self

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node, parent = root, None
        while node:
            parent = node
            if node.val < val:
                node = node.right
            else:
                node = node.left
        
        if not parent:
            return TreeNode(val)
        
        if parent.val > val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        
        return root

t = ListToTree([4, 2, 7, 1, 3])
PrintTree(t)
PrintTree(Solution().insertIntoBST(t, 5))