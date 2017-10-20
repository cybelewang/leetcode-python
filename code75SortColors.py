"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        i, j, k = 0, len(nums) - 1, 0

        while k <= j:
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                while i<=j and nums[i] == 0: i += 1
                k = max(i, k)
            elif nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                while i<=j and nums[j] == 2: j -= 1
            else:
                k += 1
        
test_cases = [[0, 0], [1, 1], [2, 2], [0, 1, 2], [2,1,2,1], [0, 0, 2, 0, 2, 0, 2, 2],[0, 0, 2, 2, 1, 0, 2, 2]]
obj = Solution()
for case in test_cases:
    print(case, end = ' -> ')
    obj.sortColors(case)
    print(case)
                
