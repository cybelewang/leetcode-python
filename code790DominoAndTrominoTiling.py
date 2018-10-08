"""
790 Domino and Tromino Tiling

We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

XX  <- domino

XX  <- "L" tromino
X
Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.

(In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.)

Example:
Input: 3
Output: 5
Explanation: 
The five different ways are listed below, different letters indicates different tiles:
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY
Note:

N  will be in range [1, 1000].
"""
class Solution:
    # DP solution from http://www.cnblogs.com/grandyang/p/9179556.html
    # analyze N = 1 to N = 5 and figure out dp[i] = 2*dp[i-1] + dp[i-3]
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp, M = [0]*(max(N,3)+1), 10**9+7
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, N+1):
            dp[i] = (2*dp[i-1] + dp[i-3])%M
        
        return dp[N]

print(Solution().numTilings(1))