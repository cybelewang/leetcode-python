"""
892. Surface Area of 3D Shapes

On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46

Note:

1 <= N <= 50
0 <= grid[i][j] <= 50
"""
class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        ans = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    ans += 1
                else:
                    # top and bottom
                    ans += 2
                    # north surfaces
                    if i == 0:
                        ans += grid[i][j]
                    else:
                        ans += 0 if grid[i][j] <= grid[i-1][j] else grid[i][j] - grid[i-1][j]
                    # west surfaces
                    if j == 0:
                        ans += grid[i][j]
                    else:
                        ans += 0 if grid[i][j] <= grid[i][j-1] else grid[i][j] - grid[i][j-1]
                    # south surfaces
                    if i == N-1:
                        ans += grid[i][j]
                    else:
                        ans += 0 if grid[i][j] <= grid[i+1][j] else grid[i][j] - grid[i+1][j]
                    # east surfaces
                    if j == N-1:
                        ans += grid[i][j]
                    else:
                        ans += 0 if grid[i][j] <= grid[i][j+1] else grid[i][j] - grid[i][j+1]
        
        return ans

grid = [[1,2],[3,4]]
print(Solution().surfaceArea(grid))