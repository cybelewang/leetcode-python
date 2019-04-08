"""
998 Maximum Binary Tree II

We are given the root node of a maximum tree: a tree where every node has a value greater than any other value in its subtree.

Just as in the previous problem, the given tree was constructed from an list A (root = Construct(A)) recursively with the following Construct(A) routine:

If A is empty, return null.
Otherwise, let A[i] be the largest element of A.  Create a root node with value A[i].
The left child of root will be Construct([A[0], A[1], ..., A[i-1]])
The right child of root will be Construct([A[i+1], A[i+2], ..., A[A.length - 1]])
Return root.
Note that we were not given A directly, only a root node root = Construct(A).

Suppose B is a copy of A with the value val appended to it.  It is guaranteed that B has unique values.

Return Construct(B).

Example 1:
Input: root = [4,1,3,null,null,2], val = 5
Output: [5,4,null,1,3,null,null,2]
Explanation: A = [1,4,2,3], B = [1,4,2,3,5]

Example 2:
Input: root = [5,2,4,null,1], val = 3
Output: [5,2,4,null,1,null,3]
Explanation: A = [2,1,5,4], B = [2,1,5,4,3]

Example 3:
Input: root = [5,2,3,null,1], val = 4
Output: [5,2,4,null,1,3]
Explanation: A = [2,1,5,3], B = [2,1,5,3,4]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    # val is appended at the end of A, so TreeNode(val) must be at the most right side
    # case 1: root.val < val, set root as the left subtree of TreeNode(val)
    # case 2: root.val > val, search along the most right nodes, stop at (1) current node's right child is null (2) current node's right child's val < val. 
    # For both conditions (1) and (2), we insert TreeNode(val) as current node's right child, and set previous right child as TreeNode(val) 's left child
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root or root.val < val:
            node = TreeNode(val)
            node.left = root
            return node
        
        node = root
        while node.right and node.right.val > val:
            node = node.right
        
        subtree = node.right
        new_node = TreeNode(val)
        node.right = new_node
        new_node.left = subtree

        return root

null = None
root = ListToTree([4,1,3,null,null,2])
PrintTree(Solution().insertIntoMaxTree(root, 5))