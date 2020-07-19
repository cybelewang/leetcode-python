"""
283 Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
 """
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1

    # 2nd round visit on 7/17/2020, bubble sort, O(N^2)
    def moveZeros(self, nums):
        i, j = 0, len(nums)
        for j in range(len(nums), 0, -1):
            for i in range(j-1):
                if nums[i] == 0:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                

test_case = [0, 1, 0, 3, 12]
obj = Solution()
obj.moveZeroes(test_case)
print(test_case)