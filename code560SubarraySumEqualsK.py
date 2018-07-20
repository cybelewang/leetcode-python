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
from collections import defaultdict, Counter
from bisect import bisect
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

if __name__ == "__main__":
    nums = [0, 0, 0]    # test this case
    print(Solution().subarraySum(nums, 0))
