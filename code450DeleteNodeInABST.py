"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # a helper TreeNode, similar to the helper node in linkedlist
        helper = TreeNode(0)
        helper.right = root

        # search the node with key
        parent, node = helper, root
        while node:
            if node.val == key:
                break
            elif node.val > key:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right
        else:
            # node not found
            return root
        
        # now move values from right child (if right child is not empty), or left child (if right child is empty), until node becomes a leaf
        while node.left or node.right:
            if node.right:
                node.val = node.right.val
                parent = node
                node = node.right
            else:
                node.val = node.left.val
                parent = node
                node = node.left
        
        # disconnect node leaf from parent
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
        
        return helper.right

null = None
root = ListToTree([5, null])
PrintTree(root)
PrintTree(Solution().deleteNode(root, 3))