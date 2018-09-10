"""
324 Wiggle Sort II

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""
class Solution:
    # use numpy module's partition to achieve similar C++'s nth_element 
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

    # sort the list first, then insert 
    def wiggleSort2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        snums = sorted(nums)
        for x in list(range(1, size, 2)) + list(range(0, size, 2)):
            nums[x] = snums.pop()

nums = [1, 3, 2, 2, 3, 1]
obj = Solution()
obj.wiggleSort(nums)
print(nums)