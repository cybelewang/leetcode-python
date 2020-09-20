"""
1091 Shortest Path in Binary Matrix

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

Example 1:

Input: [[0,1],[1,0]]

Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]

Output: 4

Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1
"""
from collections import deque
class Solution:
    # BFS solution
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        visited = [[False]*N for _ in range(N)]
        q = deque([(0, 0)])
        visited[0][0] = True
        count = 1
        while q:
            size = len(q)
            for i in range(size):
                x, y = q.popleft()
                if x == N - 1 and y == N - 1:
                    return count
                for x, y in (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1):
                    if N > x >= 0 <= y < N and grid[x][y] == 0 and not visited[x][y]:
                        q.append((x, y))
                        visited[x][y] = True
            
            count += 1
        
        return -1