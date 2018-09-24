"""
337 House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem
# very good summay about how to convert recursive solution to DP solution
from TreeNode import *
class Solution:
    # use two candidate results: one with root not robbed, and the other one with root robbed
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _rob(root):
            res = [0, 0]
            if not root:
                return res

            left, right = _rob(root.left), _rob(root.right)
            res[0] = max(left) + max(right)
            res[1] = root.val + left[0] + right[0]

            return res

        return max(_rob(root))

    # Use a map to cache the overlapping subproblems, not the best
    def rob2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _rob(root, rob, cache):
            res = 0
            if not root:
                return res
            
            if rob:
                if root in cache:
                    return cache[root]
                else:
                    res += root.val
                    res += _rob(root.left, False, cache)
                    res += _rob(root.right, False, cache)
                    cache[root] = res
            else:
                res += max(_rob(root.left, True, cache), _rob(root.left, False, cache))
                res += max(_rob(root.right, True, cache), _rob(root.right, False, cache))

            return res

        cache = {}
        return max(_rob(root, True, cache), _rob(root, False, cache))

    # recursive solution, TLE
    def rob3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _rob(root, rob):
            res = 0
            if not root:
                return res

            if rob:
                res += root.val
                res += _rob(root.left, False) 
                res += _rob(root.right, False)
            else:
                res += max(_rob(root.left, True), _rob(root.left, False))
                res += max(_rob(root.right, True), _rob(root.right, False))
            
            return res

        return max(_rob(root, True), _rob(root, False))

test_case = [2, None, 3, None, 1]
obj = Solution()
print(obj.rob(ListToTree(test_case)))