"""
883 Projection Area of 3D Shapes

On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. 

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

 

Example 1:

Input: [[2]]
Output: 5
Example 2:

Input: [[1,2],[3,4]]
Output: 17
Explanation: 
Here are the three projections ("shadows") of the shape made with each axis-aligned plane.

Example 3:

Input: [[1,0],[0,2]]
Output: 8
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 14
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 21
 

Note:

1 <= grid.length = grid[0].length <= 50
0 <= grid[i][j] <= 50
"""
class Solution:
    # my own one-pass solution
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        top = 0 
        front = [0]*n
        for i in range(m):
            side = 0
            for j in range(n):
                if grid[i][j] > 0:
                    top += 1
                side = max(side, grid[i][j])
                front[j] = max(front[j], grid[i][j])
            top += side
        
        return top + sum(front)

grid = [[1,2],[3,4]]
print(Solution().projectionArea(grid))