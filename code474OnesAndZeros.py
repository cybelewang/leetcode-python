"""
474 Ones and Zeroes

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
"""
# 0-1 knapsack? https://leetcode.com/problems/ones-and-zeroes/discuss/95808/0-1-knapsack-in-python
class Solution:
    # tried to sort strs based on length and count of 1 and 0, then greedy based on the min(m, n) but failed
    # DP method, help from http://www.cnblogs.com/grandyang/p/6188893.html
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in range(m+1)]    # dp[i][j] represents max count of strs with i 0s and j 1s
        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)

        return dp[m][n]

strs = ["10", "0001", "111001", "1", "0"]
m, n = 5, 3
print(Solution().findMaxForm(strs, m, n))