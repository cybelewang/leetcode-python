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
    # We need to find the next smallest node, and move it to the node to be deleted. See below for details
    # https://webdocs.cs.ualberta.ca/~holte/T26/del-from-bst.html
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

        def _delete(parent, node):
            # case 1: key node is a leaf node
            if node.left is None and node.right is None:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            # case 2: key node has only one subtree
            elif node.left is None or node.right is None:
                if parent.left == node:
                    parent.left = node.left or node.right
                else:
                    parent.right = node.left or node.right
            # case 3: key node has both left and right subtrees
            else:                
                # now find the smallest node in the right subtree, and use that node to replace key node
                p1, n1 = node, node.right
                while n1 and n1.left:
                    p1 = n1
                    n1 = n1.left
                # replace key node value with the next smallest node's value
                node.val = n1.val
                # recursively delete/replace the next smallest node's value with next next smallest node's value
                _delete(p1, n1)
        
        # call the _delete subfunction
        _delete(parent, node)

        return helper.right
        
    # wrong solution, we cannot just move values from right child
    def deleteNode2(self, root, key):
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
Input=[2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6]
key = 33
root = ListToTree(Input)
PrintTree(root)
PrintTree(Solution().deleteNode(root, key))

"""
Input:
[2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6]
33
Output:
[2,0,40,null,1,25,45,null,null,11,31,34,46,10,18,29,32,null,36,43,48,4,null,12,24,26,30,null,null,35,39,42,44,null,49,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41,null,null,null,47,null,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6]
Expected:
[2,0,34,null,1,25,40,null,null,11,31,35,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,null,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,38,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6]
"""