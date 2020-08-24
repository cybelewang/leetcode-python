"""
1269 Number of Ways to Stay in the Same Place After Some Steps

You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place  (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
Example 2:

Input: steps = 2, arrLen = 4
Output: 2
Explanation: There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
Example 3:

Input: steps = 4, arrLen = 2
Output: 8

Constraints:

1 <= steps <= 500
1 <= arrLen <= 10^6
"""
class Solution:
    # https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/discuss/437700/Very-simple-and-easy-to-understand-java-solution
    # dp[i][j] represents number of ways to position j in i steps
    # dp[i][j] can from 3 ways: (1) stay, this is dp[i-1][j] (2) move left, this is dp[i-1][j+1] (3) move right, this is dp[i-1][j-1]
    # max position is the min(steps, arrLen-1)
    def numWays(self, steps: int, arrLen: int) -> int:
        maxPos = min(steps, arrLen-1)
        dp = [[0]*(maxPos+1) for _ in range(steps+1)]
        dp[1][0] = 1
        dp[1][1] = 1
        M = 10**9 + 7
        for i in range(2, steps+1):
            for j in range(maxPos+1):
                dp[i][j] = dp[i-1][j]
                if j+1 <= maxPos:
                    dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % M
                if j-1 >= 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % M
        
        return dp[steps][0]  
    
    # reduce dp to 1D
    def numWays(self, steps: int, arrLen: int) -> int:
        maxPos = min(steps, arrLen-1)
        dp = [0]*(maxPos+1)
        dp[0] = dp[1] = 1
        M = 10**9 + 7
        for i in range(2, steps+1):
            pre = 0 # dp[i-1][j-1]
            for j in range(maxPos+1):
                t = dp[j]
                if j+1 <= maxPos:
                    dp[j] = (dp[j] + dp[j+1]) % M
                dp[j] = (dp[j] + pre) % M
                pre = t
        
        return dp[0] 