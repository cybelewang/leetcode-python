"""
325 Maximum Size Subarray Sum Equals k

Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
"""
class Solution:
    # solution 2 from https://www.cnblogs.com/grandyang/p/5336668.html
    # we don't need an accumulation list
    # we don't need to iterate nums twice
    def maxSubArrayLen(self, nums, k):
        mem, res = {0:-1}, 0
        _sum = 0
        for i, num in enumerate(nums):
            _sum += num
            if _sum - k in mem:
                res = max(res, i - mem[_sum-k])
            mem.setdefault(_sum, i)
        
        return res

nums, k = [1, -1, 5, -2, 3], 0
print(Solution().maxSubArrayLen(nums, k))