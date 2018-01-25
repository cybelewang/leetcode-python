"""
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # n < 3
        if n == 0 or n == 2:
            return 0
        if n == 1:
            return nums[0]

        # n >= 3
        dp = [0 for i in range(n)]

        # rob from 0 to n-2
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n-1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        max0 = dp[n-2]

        # rob from 1 to n-1
        dp[0] = 0
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        max1 = dp[n-1]

        return max(max0, max1)

nums = [1, 1, 1, 1, 11]
obj = Solution()
print(obj.rob(nums))