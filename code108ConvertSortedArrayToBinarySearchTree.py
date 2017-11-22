from TreeNode import *
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        else:
            return self._recursive(nums, 0, len(nums) - 1)

    def _recursive(self, nums, s, e):
        
        if s > e:
            return None
        elif s == e:
            return TreeNode(nums[s])
        else:
            mid = (s + e)//2
            root = TreeNode(nums[mid])
            root.left = self._recursive(nums, s, mid - 1)
            root.right = self._recursive(nums, mid + 1, e)

            return root

test_case = [1, 2, 3, 4, 5]
obj = Solution()
PrintTree(obj.sortedArrayToBST(test_case))