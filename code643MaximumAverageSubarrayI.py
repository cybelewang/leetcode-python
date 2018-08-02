"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""
class Solution:
    # my own solution using sliding window
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxsum = -2**31
        i, sum_ = 0, 0
        for j in range(len(nums)):
            sum_ += nums[j]
            if j - i + 1 == k:
                maxsum = max(maxsum, sum_)
                sum_ -= nums[i] # bug fixed: forgot to minus nums[i] before advancing i
                i += 1

        return maxsum/k

nums = [1,12,-5,-6,50,3]
print(Solution().findMaxAverage(nums, 4))