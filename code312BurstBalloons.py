"""
312 Burst Balloons

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. 
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. 
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
class Solution:
    # https://kennyzhuang.gitbooks.io/algorithms-collection/content/burst_balloons.html
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)

        dp = [[0]*n for _ in range(n)]

        for k in range(2, n):   # all possible length, note right = left + k, for left = 0, the max right will be n-1, so max of k is n-1
            for left in range(n-k): # note right = left + k, max of right is n - 1, so max of left is n - 1 - k
                right = left + k
                for i in range(left+1, right):  # all possible positions between left (exclusive) and right (exclusive)
                    # i is the last balloon to burst, so its left and right will be "left" and "right"
                    dp[left][right] = max(dp[left][right], nums[left]*nums[i]*nums[right] + dp[left][i] + dp[i][right])

        return dp[0][n-1]

test_case = [3, 1, 5, 8]
obj = Solution()
print(obj.maxCoins(test_case))