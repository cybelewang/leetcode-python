"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    # my own solution using two stacks: same and diff
    # same stores the same value nodes which are directly connected
    # diff stores the different value nodes encountered when iterating
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        same, diff, res = [], [root], 0
        while diff:
            same.append(diff.pop())
            count = -1
            while same:
                node = same.pop()
                if node.left:
                    if node.left.val == node.val:
                        same.append(node.left)
                    else:
                        diff.append(node.left)
                if node.right:
                    if node.right.val == node.val:
                        same.append(node.right)
                    else:
                        diff.append(node.right)
                count += 1
            
            res = max(res, count)

        return res

root = ListToTree([1,1,1,2,1])
print(Solution().longestUnivaluePath(root))