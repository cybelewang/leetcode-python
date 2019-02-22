"""
236 Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # recursive solution
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or root == p or root == q:
            return root

        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)

        if left_result is None:
            return right_result
        elif right_result is None:
            return left_result
        else:
            return root
    
    # 2nd round solution on 2/22/2019
    def lowestCommonAncestor2(self, root, p, q):
        if root in (p, q, None):
            return root
        
        left = self.lowestCommonAncestor2(root.left, p, q)
        # optimization when we already found LCA for p and q, removing below two lines will not affect the result
        if left and left not in (p, q):
            return left

        right = self.lowestCommonAncestor2(root.right, p, q)

        # list a truth table for left, right and result
        if left and right:
            return root
        else:
            return left or right
