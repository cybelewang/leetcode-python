"""
549 Binary Tree Longest Consecutive Sequence II

Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:
Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].

Note: All the values of tree nodes are in the range of [-1e7, 1e7].
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.ans = 0
        def helper(root):
            # return the longest increased sequence length, and longest decreased sequence length
            if not root:
                return [0, 0]
            
            li, ld = helper(root.left)
            ri, rd = helper(root.right)
            res = [1, 1]
            if root.left:
                if root.val == root.left.val + 1:
                    res[0] = max(res[0], 1 + li)
                elif root.val + 1 == root.left.val:
                    res[1] = max(res[1], 1+ ld)
                    
            if root.right:
                if root.val == root.right.val + 1:
                    res[0] = max(res[0], 1 + ri)
                elif root.val + 1 == root.right.val:
                    res[1] = max(res[1], 1 + rd)
            # update the global answer
            self.ans = max(self.ans, res[0] + res[1] - 1)
            return res
        
        helper(root)
        return self.ans