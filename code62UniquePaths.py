"""
62 Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.
"""
# To Do: try to use 1-d array for dynamic programming
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 or n < 1:
            return 0

        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1

        for i in range(1, m):
            dp[i][0] = 1

        for j in range(1, n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

test_cases = [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2), (2, 4), (3, 3), (100, 100)]

obj = Solution()
for case in test_cases:
    print(case, end = ' -> ')
    print(obj.uniquePaths(case[0],case[1]))

