"""
827 Making A Large Island

In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

Notes:

1 <= grid.length = grid[0].length <= 50.
0 <= grid[i][j] <= 1.
"""
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        def mark(i, j, color, area):
            grid[i][j] = color
            area[color] += 1
            for dx, dy in dirs:
                x, y = i+dx, j+dy
                if -1<x<m and -1<y<n and grid[x][y]==1:
                    mark(x, y, color, area)
        
        # main
        # color and count islands
        # pitfall 1: we should update result with each island's area
        color, res = 2, 0
        area = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    mark(i, j, color, area)
                    res = max(res, area[color])
                    color += 1
        
        # join different islands on each 0
        # pitfall 2: we should check if neighboring islands have been calculated
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    local = 1
                    used = set()
                    for dx, dy in dirs:
                        x, y = i+dx, j+dy
                        if -1<x<m and -1<y<n and grid[x][y] > 1 and grid[x][y] not in used:
                            local += area[grid[x][y]]
                            used.add(grid[x][y])
                    res = max(res, local)
              
        return res