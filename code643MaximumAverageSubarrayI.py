"""
643 Maximum Average Subarray I

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
    # use sliding-window coding style
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        su, res = 0, -float('INF')
        for i in range(len(nums)):
            su += nums[i]
            if i >= k:
                su -= nums[i-k]
            if i >= k-1:
                res = max(res, su/k)
        
        return res

nums = [1,12,-5,-6,50,3]
print(Solution().findMaxAverage(nums, 4))