"""
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
    #https://blog.csdn.net/qq508618087/article/details/51337187
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def index(i, n):
            return (1 + 2*i)%(n|1)

        n = len(nums)
        low, high = 0, n-1
        mid = nums[n//2]
        i = 0

        while i <= high:
            ii, ll, hh = index(i, n), index(low, n), index(high, n)
            if nums[ii] > mid:
                nums[ii], nums[ll] = nums[ll], nums[ii]
                i += 1
                low += 1
            elif nums[ii] < mid:
                nums[ii], nums[hh] = nums[hh], nums[ii]
                high -= 1
            else:
                i += 1

nums = [1, 3, 2, 2, 3, 1]
obj = Solution()
obj.wiggleSort(nums)
print(nums)