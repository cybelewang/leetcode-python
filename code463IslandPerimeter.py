"""
463 Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. 
Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). 
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
"""
class Solution:
    # iterate all elements, if element is 1 and count 1 for each neighbor 0 
    # space O(m*n)
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m < 1:
            return 0
        
        n, res = len(grid[0]), 0
        neighbors = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # left, above, right, below
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    # [i][j] is a land
                    for dx, dy in neighbors:
                        x, y = i + dx, j + dy
                        if x < 0 or x == m or y < 0 or y == n or grid[x][y]==0:
                            res += 1
        
        return res

    # O(m*n) time, O(1) space
    # count each land cell's primeter as 4, then if current land cell has above land, subtract 2 for overlay edges
    # similarily, if current land cell has left land, subtract 2 for overlay edges
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                
                    if i > 0 and grid[i-1][j] == 1:
                        res -= 2

                    if j > 0 and grid[i][j-1] == 1:
                        res -= 2
                    
        return res

grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
obj = Solution()
print(obj.islandPerimeter(grid))
