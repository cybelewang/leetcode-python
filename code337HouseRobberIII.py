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
        def helper(root):
            res = [0, 0]    # res[0] means root not robbed, res[1] means root robbed
            if not root:
                return res

            left, right = helper(root.left), helper(root.right)
            res[0] = max(left) + max(right) # root not robbed, so add left child's max and right child's max, pitfall: should not be res[0] = left[1] + right[1]
            res[1] = root.val + left[0] + right[0]  # root is robbed, so must add left child's not robbed result and right child's not robbed result

            return res

        return max(helper(root))

    # Use a map to cache the overlapping subproblems
    def rob2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, mem):
            if not root: return 0
            if root in mem:
                return mem[root]
            # don't rob root, root children and get a value
            children = helper(root.left, mem) + helper(root.right, mem)
            # rob root and grandchildren and get a value
            grand = root.val
            if root.left:
                grand += helper(root.left.left, mem) + helper(root.left.right, mem)
            if root.right:
                grand += helper(root.right.left, mem) + helper(root.right.right, mem)
            # take the max one
            mem[root] = max(children, grand)
            return mem[root]
        
        mem = {}        
        return helper(root, mem)

    # recursive solution, TLE
    def rob3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, canRob):
            if not root: return 0
            robSubtree = helper(root.left, True) + helper(root.right, True)
            notRobSubtree = helper(root.left, False) + helper(root.right, False)
            if canRob:
                # can rob root, two cases: rob root, or not rob root
                return max(root.val + notRobSubtree, robSubtree)
            else:
                # cannot rob root
                return robSubtree
        
        return helper(root, True)

test_case = [3, 2, 3, None, 3, None, 1]
obj = Solution()
print(obj.rob2(ListToTree(test_case)))