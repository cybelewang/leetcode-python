"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_, mem = 0, defaultdict(int) # default value is 0, for other values, use lambda: value
        mem[0] = 1
        for num in nums:
            sum_ += num
            mem[sum_] += 1
        
        res = 0

        return res

if __name__ == "__main__":
    nums = [1, 1, 1]    # test this case
    print(Solution().subarraySum(nums, 2))
