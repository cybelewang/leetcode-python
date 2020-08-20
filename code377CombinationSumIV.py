"""
377 Combination Sum IV

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
class Solution:
    # DP
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0]*(1+target)
        dp[0] = 1
        for t in range(1, 1+target):
            for num in nums:
                if t >= num:
                    dp[t] += dp[t-num]
        return dp[t]

    # recursive + memo
    def combinationSum5(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def count(target, memo):
            if target == 0:
                return 1
            elif target < 0:
                return 0
            else:
                if target in memo:
                    return memo[target]

                res = 0
                for num in nums:
                    res += count(target - num, memo)
                memo[target] = res
                return res
        
        nums.sort()
        memo = {}
        return count(target, memo)

nums, target = [4, 1, 2], 32
obj = Solution()
print(obj.combinationSum4(nums, target))