"""
1020 Number of Enclaves

Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:
Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.

Example 2:
Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: 
All 1s are either on the boundary or can reach the boundary.

Note:

1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.
"""
from collections import deque
class Solution:
    # my own BFS solution
    def numEnclaves(self, A):
        """
        :type A: list[list[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        res = 0
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    A[i][j] = -1    # -1 means visited
                    q = deque([(i, j)])
                    count = 0
                    bWalkOff = False
                    while q:
                        x, y = q.popleft()
                        count += 1
                        if x == 0 or x == m-1 or y == 0 or y == n-1:
                            bWalkOff = True
                        for dx, dy in dirs:
                            a, b = x + dx, y + dy
                            if -1 < a < m and -1 < b < n and A[a][b] == 1:
                                A[a][b] = -1
                                q.append((a, b))
                    
                    if not bWalkOff:
                        res += count
        
        return res

A = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]   #expect 0
print(Solution().numEnclaves(A))
