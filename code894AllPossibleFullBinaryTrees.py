"""
894 All Possible Full Binary Trees

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:

Note:

1 <= N <= 20
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import *
from collections import defaultdict
class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N < 1 or N & 0x01 == 0:
            return []
        
        fbt = defaultdict(list)
        fbt[1].append(TreeNode(0))
        for n in range(3, N+1, 2):
            # n - 1 is the remaining nodes
            for i in range(1, n-1, 2):
                j = n - 1 - i
                for left in fbt[i]:
                    for right in fbt[j]:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        fbt[n].append(root)
        
        return fbt[N]

