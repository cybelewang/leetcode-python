"""
637 Average of Levels in Binary Tree

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
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
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        if not root:
            return res

        q = deque()
        q.append(root)

        while q:
            len_, avg = len(q), 0
            for i in range(len_):
                node = q.popleft()
                avg = avg + (node.val - avg)/(i+1)  # Cumulative moving average: https://en.wikipedia.org/wiki/Moving_average
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(avg)
        
        return res

t = ListToTree([3,9,20,None, None, 15, 7])
PrintTree(t)
print(Solution().averageOfLevels(t))