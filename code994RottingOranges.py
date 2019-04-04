"""
994 Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""
from collections import deque
class Solution:
    def orangesRotting(self, grid):
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if all(grid[i][j] == 0 for i in range(m) for j in range(n)):
            return 0

        q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2])
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
      
        t = 0
        while q:
            t += 1
            _len = len(q)
            for _ in range(_len):
                x, y = q.popleft()
                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if -1 < i < m and -1 < j < n and grid[i][j] == 1:
                        q.append((i, j))
                        grid[i][j] = 2

        if any(grid[i][j] == 1 for i in range(m) for j in range(n)):
            return -1
        else:
            return t-1

#grid =[[0]]     # expect 0
#grid = [[1]]    # expect -1
#grid = [[2]]    # expect 0
grid = [[2,1,1],[1,1,0],[0,1,1]]    # expect 4
print(Solution().orangesRotting(grid))