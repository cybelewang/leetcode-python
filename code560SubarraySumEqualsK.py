"""
560 Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
# similar problems: 523, 594 Longest Harmonious Subsequence
from collections import defaultdict, Counter
from bisect import bisect
import unittest
class Solution:
    # see https://leetcode.com/problems/subarray-sum-equals-k/discuss/102111/Python-Simple-with-Explanation
    def subarraySum_OJBEST(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = Counter()
        count[0] = 1
        ans = su = 0
        for x in nums:
            su += x
            ans += count[su-k]
            count[su] += 1
        return ans
    
    # my own solution
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_, mem = 0, defaultdict(list)    # mem is a dict with key of the accumulated sum, value of a list holding all indices of this accumulated sum
        for i, num in enumerate(nums):
            sum_ += num
            mem[sum_].append(i)
        
        res = 0
        if k in mem:
            res += len(mem[k])   # subarrays start from beginning position
        
        if k == 0:
            for key in mem:
                res += len(mem[key])*(len(mem[key]) - 1)//2   # if k == 0, calculate the combinations = C(n, 2)
        else:        
            for key in mem:
                if k + key in mem:
                    for left in mem[key]:
                        right = bisect(mem[k+key], left)
                        res += len(mem[k+key]) - right
                    # below is wrong because we need to consider the sequence: k + key must be after key
                    #res += mem[key] * mem[k+key]    # if k != 0, one end has mem[key] selections and other end has mem[k+key] selections

        return res

    # FB interview question, follow-up: if all integers are non-negative, use sliding windows
    # must handle k == 0 specially because sliding window will advance left pointer in one direction
    # cannot pass test case ([0,1,0],1) == 4
    def subarraySum_NonNegative(self, nums, k):
        def countZeros(nums):
            zeros, cnt = 0, 0
            for num in nums:
                if num == 0:
                    zeros += 1
                    cnt += zeros
                else:
                    zeros = 0
            return cnt
        
        # handle k == 0 specially
        if k == 0: return countZeros(nums)
        # k != 0
        i, res = 0, 0
        su = 0
        for j in range(len(nums)):
            su += nums[j]
            while i <= j and su >= k:  
                if su == k: res += 1                
                su -= nums[i]                             
                i += 1
        
        return res

    # see https://www.1point3acres.com/bbs/thread-651563-5-1.html
    # cannot pass test case ([0,1,0],1)=4
    def subarraySum3(self, nums, k):
            if not nums:
                    return 1 if k == 0 else 0
            l, r = 0, 0
            n = len(nums)
            cur_sum = 0
            result = 0
            while (l < n and r < n):
                    cur_sum += nums[r]
                    while l <= r and cur_sum > k:
                            cur_sum -= nums[l]
                            l += 1
                    next_l = l  # Remove comment to pass the last test case ([0,0,0,0,0], 0) == 15
                    while l <= r and cur_sum == k:
                            result += 1
                            l += 1
                    l = next_l  # Remove comment to pass the last test case ([0,0,0,0,0], 0) == 15
                    r += 1
            return result

class Test(unittest.TestCase):
    def test_1(self):
        obj = Solution()
        self.assertEqual(obj.subarraySum_OJBEST([1,1,1], 2), 2)
        self.assertEqual(obj.subarraySum_NonNegative([1,1,1],2), 2)
        self.assertEqual(obj.subarraySum_NonNegative([0,0,0],1), 0)
        self.assertEqual(obj.subarraySum_NonNegative([0,0,0],0), 6)
        self.assertEqual(obj.subarraySum3([0,1,0],1), 4)
if __name__ == "__main__":
    unittest.main(exit=False)
