"""
747 Largest Number At Least Twice of Others

In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
 

Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
"""
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return -1
        
        # top1, top2 are indices of largest and 2nd largest number in nums
        top1 = 0 if nums[0] > nums[1] else 1
        top2 = 0 if nums[0] < nums[1] else 1

        for i in range(2, n):
            if nums[i] > nums[top1]:
                top1, top2 = i, top1
            elif nums[i] > nums[top2]:
                top2 = i
        
        return top1 if nums[top1] >= 2*nums[top2] else -1

test_nums = [[3, 6, 1, 0], [1, 2, 3, 4], [2, 1,1,1], [1, 1, 1, 2]]
obj = Solution()
for nums in test_nums:
    print(obj.dominantIndex(nums))