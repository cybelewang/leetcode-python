from TreeNode import *
"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 0. while node is not None
# 1. if node.left is None, continue to node.right
# 2. if node.left is not None, find the most right leaf node in the left branch, and link its right pointer to node.right. 
#    Then assign node.right to node.left and make node.left as None 

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        node = root
        while node:
            if node.left is not None:
                # go to the left branch
                pre = node.left
                # find the leaf node which is just before the right branch in preorder traversal
                while pre.left is not None or pre.right is not None:
                    if pre.right is not None:
                        pre = pre.right
                    else:
                        pre = pre.left

                pre.right = node.right
                node.right = node.left
                node.left = None
            
            node = node.right

obj = Solution()
null = None
test_case = [1, 2, 5, null, 3, null, null, 4]
test_tree = ListToTree(test_case)
PrintTree(test_tree)
obj.flatten(test_tree)
PrintTree(test_tree)          
