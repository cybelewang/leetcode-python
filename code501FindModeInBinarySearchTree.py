"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/6436150.html
    # inorder traversal, count the same value appearance
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.prev = None    # previous node's value
        self.cnt = 1    # count of the same value. bug fixed: should not be initialized to 0. Why?
        self.max = 0    # max of self.cnt
        self.res = []   # result

        def inorder(root):
            """
            inorder traversal of the BST
            """
            if root is None:
                return
            ## process left
            inorder(root.left)

            ## process root
            # update count
            if self.prev:
                self.cnt = self.cnt + 1 if root.val == self.prev else 1

            # update max and res
            if self.cnt >= self.max:
                if self.cnt > self.max: self.res.clear()
                self.max = self.cnt
                self.res.append(root.val)
            # update prev
            self.prev = root.val

            ## process right            
            inorder(root.right)
        
        # main
        inorder(root)
        return self.res

root = ListToTree([0,None,0])
PrintTree(root)
print(Solution().findMode(root))