"""
100 Same Tree

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # preorder traversal (including null nodes) is the unique identifier of a binary tree
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def G(root):
            if not root:
                yield '#'
            else:
                yield str(root.val)
                yield from G(root.left)
                yield from G(root.right)
            
        return all(a==b for a, b in zip_longest(G(p), G(q)))

test_cases = [([1,2,3],[1,2,3]), ([1,2],[1,None,2])]
obj = Solution()
for case in test_cases:
    p = ListToTree(case[0])
    q = ListToTree(case[1])
    print(obj.isSameTree(p,q))