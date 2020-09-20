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

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution(object):
    # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C%2B%2BJavaPythonRuby
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                    for kid in (root.left, root.right))
        return root if left and right else left or right
    # recursive solution
    # https://www.cnblogs.com/grandyang/p/4641968.html
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        # below is the trick: left is not None, and left is not p or q, this means we have found the LCA of p and q, so return early
        if left not in (None, p, q):
            return left

        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right
    
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

    # see C++ solution, easy to understand
    # bit encoding, 0 means not found, 1 means found p, 2 means found q
    # handles case when p or q doesn't exist in tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def helper(root):
            nonlocal res
            if not root:
                return 0
            left = helper(root.left)
            if left == 3:
                return 3
            right = helper(root.right)
            if right == 3:
                return 3
            
            encode = (root == p) | ((root == q) << 1)         
            encode = encode | left | right
            if encode == 3:
                res = root
            
            return encode
            
        helper(root)
        return res

    # follow-up: what if every node has link to parent? (FB interview question)
    # bottom-up traversal, and put all visited nodes (including p, q) into a hash set, so when a node is already visited before, that node is the LCA
    # we can also not use hash set, but use method 160 Intersection of Two Linked Lists, O(1) space
    def lowestCommonAncestor2(self, root, p, q):
        # recursively link node to parent node
        def find(root, target, parent=None):
            if not root: return False
            root.parent = parent
            if root == target: return True
            return find(root.left, target, root) or find(root.right, target, root)       
        
        # build parent link
        pExists = find(root, p)
        qExists = find(root, q)        
        # find common parent, use method in 160 Intersection of Two Linked Lists
        if pExists and qExists:
            pHead, qHead = p, q
            while p != q:
                p = p.parent if p else qHead
                q = q.parent if q else pHead
            return p
        
        return None
