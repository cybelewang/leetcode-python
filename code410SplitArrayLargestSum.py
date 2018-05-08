"""
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
 Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
# similar to Reverse Pairs
# http://www.cnblogs.com/grandyang/p/5933787.html, method 2
class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        dp = [[2**31-1]*(n+1) for _ in range(m+1)] # dp[i][j] means the minimum largest sum among i subarrays for j integers
        dp[0][0] = 0

        # build the sums list to quickly get a range sum
        sums = [0]*(n+1)
        for i in range(1, n+1):
            sums[i] = sums[i-1] + nums[i-1]

        for i in range(1, m+1):
            for j in range(i, n+1):
                for k in range(i-1, j):
                    val = max(dp[i-1][k], sums[j]-sums[k])
                    dp[i][j] = min(dp[i][j], val)
        
        return dp[m][n]

nums, m = [7,2,5,10,8], 2
obj = Solution()
print(obj.splitArray(nums, m))