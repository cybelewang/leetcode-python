"""
543 Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import *
class Solution:
    # my own solution by finding the longest path in left subtree and right subtree separately, then add them and update the result
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def longest_path(root):
            """
            find the longest path of the subtree with root
            """
            if not root:
                return -1
            
            left = 1 + longest_path(root.left)
            right = 1 + longest_path(root.right)

            self.res = max(self.res, left + right)
            return max(left, right)

        # main
        longest_path(root)

        return self.res

root = ListToTree([1, 2, None, 3, 4, 5, None, 6])
PrintTree(root)
print(Solution().diameterOfBinaryTree(root))
