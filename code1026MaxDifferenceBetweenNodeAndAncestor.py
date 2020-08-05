"""
1026 Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

Example 1:
Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 
Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import *
class Solution:
    # https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/discuss/274610/JavaC%2B%2BPython-Top-Down
    def maxAncestorDiff_singleline(self, root, mn=100000, mx=0):
        return max(self.maxAncestorDiff_singleline(root.left, min(mn, root.val), max(mx, root.val)), \
            self.maxAncestorDiff_singleline(root.right, min(mn, root.val), max(mx, root.val))) \
            if root else mx - mn
            
    # my own DFS solution, tracking the pair of (min, max) for subtree
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.V = 0
        def helper(root, minVal, maxVal):
            if not root:
                return
            self.V = max(self.V, abs(root.val-minVal), abs(maxVal-root.val))
            minVal = min(root.val, minVal)
            maxVal = max(root.val, maxVal)
            helper(root.left, minVal, maxVal)
            helper(root.right, minVal, maxVal)
            
        helper(root, root.val, root.val)
        return self.V

null = None
root = ListToTree([8,3,10,1,6,null,14,null,null,4,7,13])
print(Solution().maxAncestorDiff(root))
