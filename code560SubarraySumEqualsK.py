"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
# similar problems: 523
from collections import defaultdict
class Solution:
    # my own solution
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_, mem = 0, defaultdict(int) # default value is 0, for other values, use lambda: value
        for num in nums:
            sum_ += num
            mem[sum_] += 1
        
        res = 0
        if k in mem:
            res += mem[k]   # subarray starts from beginning position
        
        if k == 0:
            for key in mem:
                res += mem[key]*(mem[key] - 1)//2   # if k == 0, calculate the combinations = C(n, 2)
        else:        
            for key in mem:
                if k + key in mem:
                    res += mem[key] * mem[k+key]    # if k != 0, one end has mem[key] selections and other end has mem[k+key] selections

        return res

if __name__ == "__main__":
    nums = [-1, -1, 1]    # test this case
    print(Solution().subarraySum(nums, 1))
