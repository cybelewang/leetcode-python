"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
"""
# http://www.cnblogs.com/grandyang/p/5677550.html
class Solution:
    # DP
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in range(n+1)]

        for j in range(2, n+1):
            for i in range(j-1, -1, -1):
                global_min = 2**31 - 1 # MAX_INT
                for k in range(i+1, j):
                    local_max = k + max(dp[i][k-1], dp[k+1][j]) # dp[i][k-1] was calculated in previous dp[i][j] where j = k -1
                    global_min = min(global_min, local_max)
                
                dp[i][j] = j if i+1==j else global_min

        return dp[1][n]

    # recursive + memory
    def getMoneyAmount2(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(start, end, memo):
            if start >= end: return 0
            if (memo[start][end] > 0): return memo[start][end]
            res = 2**31 - 1
            for k in range(start, end+1):
                t = k + max(helper(start, k-1, memo), helper(k+1, end, memo))
                res = min(res, t)
            memo[start][end] = res

            return res

        memo = [[0]*(n+1) for _ in range(n+1)]

        return helper(1, n, memo)

obj = Solution()
print(obj.getMoneyAmount(10))    