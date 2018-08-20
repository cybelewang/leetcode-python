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
    # recursive solution
    def longestUnivaluePath2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def dfs(root):
            if not root:
                return 0

            left, right = dfs(root.left), dfs(root.right)   # we always recursively call the recursive function so all nodes will be visited            
            left = 1 + left if root.left and root.left.val == root.val else 0
            right = 1 + right if root.right and root.right.val == root.val else 0

            self.res = max(self.res, left + right)

            return max(left, right)

        # main
        dfs(root)

        return self.res    

    # WRONG SOLUTION! The problem requires longest path, not count of nodes.
    # my own solution using two stacks: same and diff
    # same stores the same value nodes which are directly connected
    # diff stores the different value nodes encountered when iterating
    def longestUnivaluePath3(self, root):
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

null = None
nums = [26,26,26,26,26,24,26,25,25,25,27,23,25,25,27,24,26,24,26,24,24,null,28,null,null,26,null,null,26,26,28,25,null,25,27,null,null,null,null,null,23,null,null,29,27,null,null,null,null,25,null,27,27,24,26,24,26,26,26,null,22,28,null,26,26,null,null,26,null,28,28,25,null,null,null,25,25,25,27,25,25,27,25,null,null,null,null,null,null,null,27,27,27,null,null,27,29,24,26,26,26,null,26,null,26,null,null,null,24,24,24,null,26,24,26,null,null,null,26,null,null,null,28,null,30,null,23,27,null,null,null,null,null,null,null,null,null,null,null,23,25,25,25,27,25,23,25,null,null,null,null,null,null,29,null,null,null,26,null,22,null,null,26,24,26,null,26,28,null,null,26,22,null,null,null,null,null,null,null,null,null,null,25,23,null,null,null,null,27]

root = ListToTree(nums)
PrintTree(root)
print(Solution().longestUnivaluePath2(root))