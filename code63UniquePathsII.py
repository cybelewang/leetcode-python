"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0

        m = len(obstacleGrid)
        if m == 0:  # this handles []
            return 0
        n = len(obstacleGrid[0])
        if n == 0:  # bug fixed: we need to handle [[]]
            return 0

        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        for i in range(1, m):
            if dp[i-1][0] == 1 and obstacleGrid[i][0] == 0: # bug here: because dp[0][0] is always 0, dp[:][0] will be always 0
                dp[i][0] = 1
            else:
                dp[i][0] = 0
        
        for j in range(1, n):
            if dp[0][j-1] == 1 and obstacleGrid[0][j] == 0: # bug here: because dp[0][0] is always 0, dp[0][:] will be always 0
                dp[0][j] = 1
            else:
                dp[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

test_case = [[0, 0], [1, 0]]
obj = Solution()
print(obj.uniquePathsWithObstacles(test_case))
        