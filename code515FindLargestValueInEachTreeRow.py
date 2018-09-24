"""
515 Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import *
from collections import deque
class Solution:
    # my own BFS solution
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res

        q = deque()
        q.append(root)

        while q:
            length = len(q)
            row_max = -2**31    # becareful that this -2**31 may be included in the result if we append None to the right of dequeue
            for _ in range(length):
                node = q.popleft()

                row_max = max(row_max, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(row_max)

        return res

root = ListToTree([1, 2, 3, 4, None, 5, 6, None, None, 7])
PrintTree(root)
print(Solution().largestValues(root))         