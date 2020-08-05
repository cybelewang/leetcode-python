"""
317 Shortest Distance from All Buildings

You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:
Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""
import unittest
from collections import deque
import copy
class Solution:
    # BFS level scan, "typical BFS"
    # We will use a 2D matrix dist to sum the distance to buildings
    # The trick is that for each node with initial value 0, we need to track how many buildings reach to it in BFS
    # To get final result, we need to scan the final dist matrix and count those distance with all buildings
    def shortestDistance(self, grid):
        INT_MAX = 2**31 - 1
        m, n = len(grid), len(grid[0])
        dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        cnt, buildingCnt = copy.deepcopy(grid), 0
        dist = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildingCnt += 1
                    q = deque([(i, j)])
                    visited = [[False]*n for _ in range(m)]
                    level = 1
                    while q:
                        length = len(q)
                        for _ in range(length):
                            a, b = q.popleft()
                            for dx, dy in dirs:
                                x, y = a + dx, b + dy
                                if -1 < x < m and -1 < y < n and grid[x][y] == 0 and not visited[x][y]:
                                    q.append((x, y))
                                    visited[x][y] = True
                                    dist[x][y] += level
                                    cnt[x][y] += 1
                        level += 1
        
        res = INT_MAX
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and cnt[i][j] == buildingCnt:
                    res = min(res, dist[i][j])

        return res if res != INT_MAX else -1

    # solution 1 in https://www.cnblogs.com/grandyang/p/5297683.html
    # the basic idea is to limit the next level's scan to current level's scanned positions by decreasing grid[i][j] (or id) by 1
    # so in first BFS while loop, scan those nodes with value 0
    # in second BFS while loop, scan nodes with value -1
    # in third BFS while loop, scan nodes with value -2...
    # In this way, each BFS always scans the previously scanned nodes and also we don't need the "visited" matrix.
    # and lastly we can use a global variable res to save the shortest distance
    def shortestDistance2(self, grid):
        INT_MAX = 2**31-1
        m, n = len(grid), len(grid[0])
        res, id = INT_MAX, 0

        sum = copy.deepcopy(grid)
        dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]   # 4 directions

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = INT_MAX
                    dist = copy.deepcopy(grid)
                    q = deque([(i, j)])
                    while q:
                        a, b = q.popleft()
                        for dx, dy in dirs:
                            x, y = a + dx, b + dy
                            if -1 < x < m and -1 < y < n and grid[x][y] == id:
                                grid[x][y] -= 1
                                dist[x][y] = dist[a][b] + 1
                                sum[x][y] += dist[x][y] - 1 # dist is a copy of grid, and the building has a value of 1, so we must decrease 1 to compensate this additional 1
                                q.append((x, y))
                                res = min(res, sum[x][y])
                    id -= 1
        
        return res if res != INT_MAX else -1

    # 8/4/2020
    # BFS to build dist matrix
    def shortestDistance3(self, grid):
        m, n = len(grid), len(grid[0])
        count = [[0]*n for _ in range(m)]
        dist = [[0]*n for _ in range(m)]
        cntBuildings = 0
        dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        def bfs(i, j):
            q = deque([(i, j)])
            level = 0
            visited = set()
            while q:
                length = len(q)
                for _ in range(length):
                    i, j = q.popleft()
                    count[i][j] += 1
                    dist[i][j] += level
                    for dx, dy in dirs:
                        x, y = i + dx, j + dy
                        if -1 < x < m and -1 <y < n and grid[x][y] == 0 and (x, y) not in visited: # bug fixed: forgot to use visited set
                            q.append((x, y))
                            visited.add((x, y))
                level += 1
        
        # main
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cntBuildings += 1
                    bfs(i, j)
        # get result
        res = 2**31-1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and count[i][j] == cntBuildings:
                    res = min(res, dist[i][j])
                    
        return res if res < 2**31-1 else -1

class Test(unittest.TestCase):
    def test_1(self):
        obj = Solution()
        grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
        self.assertEqual(obj.shortestDistance(grid), 7)

if __name__ == "__main__":
    unittest.main(exit=False)