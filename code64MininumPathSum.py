"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        m = len(grid)
        if m < 1:   # handles grid == []
            return 0

        n = len(grid[0])
        if n < 1: # handles grid == [[]]
            return 0

        # Initialize the top row
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        # Initialize the left column
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])   # Always choose the less one of left and top neighbors to add
        
        return grid[m-1][n-1]

obj = Solution()
test_case = [[1, 2], [0, 4]]
print(obj.minPathSum(test_case))