"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. 
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""
from collections import defaultdict
class Solution:
    def findTargetSumWays_OJBest(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        if total < S or (total + S) & 1:
            return 0
        target = (S + total) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for n in nums:
            for i in range(target, n-1, -1):
                dp[i] += dp[i - n]
        return dp[target]
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sum_ = sum(nums)
        if S > sum_ or S < -sum_:
            return 0
        
        mem1 = defaultdict(int)
        mem1[0] = 1 # bug fixed: '0' is the seed, so other numbers can be added to it, so its count should be initialize to 1, not 0
        for num in nums:
            mem2 = defaultdict(int)
            for s in list(mem1):
                mem2[s+num] += mem1[s]
                mem2[s-num] += mem1[s]
            mem1 = mem2
            #print(mem1)
        return mem1[S]

nums = [1, 1, 1, 1, 1]
obj = Solution()
print(obj.findTargetSumWays(nums, 3))