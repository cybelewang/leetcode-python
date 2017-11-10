"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        cur = root
        while cur.left is not None:
            cur = cur.left

        preNode = cur   # previous node to be compared
        
        cur = root
        abnormal = None
        
        while cur:
            if cur.left is None:
                if cur.val < preNode.val:
                    