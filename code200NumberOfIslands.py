"""
200 Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""
from collections import deque
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
 
        def bfs(grid, m, n, queue, color):
            while len(queue) > 0:
                (i, j) = queue.popleft()
                if -1<i< m and -1<j<n and grid[i][j] == '1':
                    grid[i][j] = str(color)
                    queue.append((i, j-1))    # left
                    queue.append((i, j+1))    # right
                    queue.append((i-1, j))    # top
                    queue.append((i+1, j))    # bottom

        m, n = len(grid), len(grid[0])
        color = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    queue = deque()
                    queue.append((i, j))
                    bfs(grid, m, n, queue, color)
                    color += 1
        
        #print(grid)
        return color - 2

test_case = [
    ['1','1','0','0','0'],
    ['0','1','1','0','0'],
    ['0','0','0','1','1']
]
obj = Solution()
print(obj.numIslands(test_case))
                    