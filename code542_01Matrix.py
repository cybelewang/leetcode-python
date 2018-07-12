"""

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""
# 1st trial TLE: iterate the matrix, for each 0, update all other 1s' distance
from collections import deque
class Solution:
    # Two-pass solution: first pass update value from left top cells, second pass update value from bottom right cells
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        INT_MAX = 2**31-1
        m = len(matrix)
        if m < 1:
            return matrix
        n = len(matrix[0])

        # update all '1' to INT_MAX - 1 (why -1? because we need to add 1 later)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = INT_MAX - 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    if i > 0:
                        matrix[i][j] = min(matrix[i][j], matrix[i-1][j] + 1)    # update from top
                    if j > 0:
                        matrix[i][j] = min(matrix[i][j], matrix[i][j-1] + 1)    # update from left

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] != 0:
                    if i < m - 1:
                        matrix[i][j] = min(matrix[i][j], matrix[i+1][j] + 1)    # update from bottom
                    if j < n - 1:
                        matrix[i][j] = min(matrix[i][j], matrix[i][j+1] + 1)    # update from right

        return matrix

    # BFS solution from solution 1 in http://www.cnblogs.com/grandyang/p/6602288.html
    def updateMatrix2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if m < 1:
            return matrix

        n = len(matrix[0])
        neighbors = [[0, -1], [-1, 0], [0, 1], [1, 0]]

        # first iterate all elements, push 0 to queue, and set 1 to INT_MAX
        q = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = 2**31 - 1

        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                cur = matrix[i][j]
                for dx, dy in neighbors:
                    x, y = i + dx, j + dy
                    if -1 < x < m and -1 < y < n:
                        if matrix[x][y] <= cur + 1: # bug fixed: initially used: if matrix[x][y] < 2
                            continue
                        matrix[x][y] = min(matrix[x][y], cur + 1)
                        q.append((x, y))
        
        return matrix

matrix = [[0,1,1], [0,1,1], [1,1,1]]
print(Solution().updateMatrix(matrix))
