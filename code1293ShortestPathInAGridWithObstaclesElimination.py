"""
1293 Shortest Path in a Grid with Obstacles Elimination

Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

Example 1:

Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Example 2:

Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
 
Constraints:

grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0
"""
from collections import deque
class Solution:
    # BFS solution
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([(0, 0, k)])
        visited = set([(0, 0, k)])
        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j, remain = q.popleft()
                if (i, j) == (m-1, n-1):
                    return steps
                for x, y in (i, j-1), (i-1, j), (i, j+1), (i+1, j):
                    if m > x >= 0 <= y < n:
                        if grid[x][y] == 0 and (x, y, remain) not in visited:
                            q.append((x, y, remain))
                            visited.add((x, y, remain))
                        elif grid[x][y] == 1 and remain > 0 and (x, y, remain-1) not in visited:
                            q.append((x, y, remain - 1))
                            visited.add((x, y, remain - 1))
            steps += 1
        
        return -1