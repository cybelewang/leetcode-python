"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
from heapq import heappush, heappop
class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        neighbors = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        # pacific
        pacific = set()
        queue = []
        visited = set()
        for i in range(m):
            heappush(queue, (matrix[i][0], i, 0))
            pacific.add((i, 0))
            visited.add((i, 0))
        
        for j in range(1, n):
            heappush(queue, (matrix[0][j], 0, j))
            pacific.add((0, j))
            visited.add((0, j))

        self.bfs(matrix, m, n, queue, neighbors, pacific, visited)
        #print(pacific)

        # atlantic
        queue.clear()
        visited.clear()
        atlantic = set()
        for i in range(m):
            heappush(queue, (matrix[i][n-1], i, n-1))
            atlantic.add((i, n-1))
            visited.add((i, n-1))
        
        for j in range(n-1):
            heappush(queue, (matrix[m-1][j], m-1, j))
            atlantic.add((m-1, j))
            visited.add((m-1, j))

        self.bfs(matrix, m, n, queue, neighbors, atlantic, visited)
        #print(atlantic)

        return list(map(list, pacific & atlantic))

    def bfs(self, matrix, m, n, queue, neighbors, ocean, visited):
        while queue:
            h, x, y = heappop(queue)
            for dx, dy in neighbors:
                i, j = x + dx, y + dy
                if -1 < i < m and -1 < j < n and (i, j) not in visited:
                    visited.add((i, j))
                    if h <= matrix[i][j]:
                        heappush(queue, (matrix[i][j], i, j))
                        ocean.add((i, j))
        
matrix = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1,1, 2, 4]]
obj = Solution()
print(obj.pacificAtlantic(matrix))