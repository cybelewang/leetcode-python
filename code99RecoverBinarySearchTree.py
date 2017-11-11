from TreeNode import *
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

# Use Morris inorder traversal to get the O(1) space solution. 
class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        first, second = None, None  # the two swap TreeNodes
        pre = TreeNode(-2**31)  # Don't know what to compare for the first TreeNode? Create one!

        cur = root
        
        while cur:
            if cur.left is None:
                if cur.val < pre.val:   # Always assign pre to first, cur to second, including the case swapping two neighboring TreeNodes
                    if first is None:
                        first = pre
                    second = cur
                pre = cur
                cur = cur.right
            else:
                p = cur.left
                while p.right is not None and p.right != cur:
                    p = p.right
                if p.right is None:
                    p.right = cur
                    cur = cur.left
                if p.right == cur:
                    if cur.val < pre.val:
                        if first is None:
                            first = pre
                        second = cur
                    p.right = None  # bug fixed here: don't forget to remove the link
                    pre = cur
                    cur = cur.right
        
        # swap two nodes. Why first and second are not None? Because there are at least two TreeNodes.
        first.val, second.val = second.val, first.val

test_case = [0, 1]
test_tree = ListToTree(test_case)
obj = Solution()
obj.recoverTree(test_tree)
PrintTree(test_tree)