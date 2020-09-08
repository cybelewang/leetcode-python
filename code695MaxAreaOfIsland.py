"""
695 Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
class Solution:
    # https://leetcode.com/problems/max-area-of-island/discuss/108565/4-lines
    def maxAreaOfIsland(self, grid):
        grid = {i + j*1j: val for i, row in enumerate(grid) for j, val in enumerate(row)}
        def area(z):
            return grid.pop(z, 0) and 1 + sum(area(z + 1j**k) for k in range(4))
        return max(map(area, set(grid)))
    # my own solution of coloring the pixels
    def maxAreaOfIsland2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def area(i, j, color):
            ans = 1
            for i, j in (i, j-1), (i-1, j), (i, j+1), (i+1, j):
                if m > i >= 0 <= j < n and grid[i][j] == 1:
                    grid[i][j] = color
                    ans += area(i, j, color)
            return ans
        
        color, res = 2, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = color
                    res = max(res, area(i, j, color))
                    color += 1
        return res


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,1,1,0,1,0,0,0,0,0,0,0,0], [0,1,0,0,1,1,0,0,1,0,1,0,0], [0,1,0,0,1,1,0,0,1,1,1,0,0], [0,0,0,0,0,0,0,0,0,0,1,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,0,0,0,0,0,0,1,1,0,0,0,0]]
obj = Solution()
print(obj.maxAreaOfIsland(grid))