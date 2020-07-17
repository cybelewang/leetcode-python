from TreeNode import *
"""
114 Flatten Binary Tree to Linked List

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

# similar problems: 897 Increasing Order Search Tree
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
                # link the leaf node's right child to the right branch
                pre.right = node.right
                # link the right branch to the left branch
                node.right = node.left
                # assign left branch to null
                node.left = None
            
            node = node.right

    # 2nd round solution on 12/9/2018
    # similar solution as 897
    def flatten2(self, root):
        def helper(root):
            if not root:
                return (None, None)
            head1, tail1 = helper(root.left)
            head2, tail2 = helper(root.right)
            node = root
            if head1:
                node.left = None
                node.right = head1
                node = tail1
            if head2:
                node.left = None
                node.right = head2
                node = tail2

            return (root, node)
        
        # main
        helper(root)
    
    # 3rd round solution on 7/15/2020
    # recursive solution
    def flatten3(self, root):
        def helper(root):
            if not root: return None
            left, right = root.left, root.right
            tail = root
            if left:
                tail.left = None
                tail.right = left
                tail = helper(left)
            if right:
                tail.left = None
                tail.right = right
                tail = helper(right)

            return tail
        # main
        helper(root)


obj = Solution()
null = None
test_case = [1, 2, 5, null, 3, null, null, 4]
test_tree = ListToTree(test_case)
PrintTree(test_tree)
obj.flatten3(test_tree)
PrintTree(test_tree)          
