"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
from collections import deque
class Solution:
    # DFS + Cache
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def _getLongestPath(matrix, m, n, i, j, mem):
            if mem[i][j] > 0:
                return mem[i][j]
            else:
                curVal = matrix[i][j]
                count = 1   # include this number itself
                # left
                if j > 0 and matrix[i][j-1] > curVal:
                    count = max(count, 1 + _getLongestPath(matrix, m, n, i, j-1, mem))
                # right
                if j < n-1 and matrix[i][j+1] > curVal:
                    count = max(count, 1 + _getLongestPath(matrix, m, n, i, j+1, mem))
                # top
                if i > 0 and matrix[i-1][j] > curVal:
                    count = max(count, 1 + _getLongestPath(matrix, m, n, i-1, j, mem))
                # below
                if i < m-1 and matrix[i+1][j] > curVal:
                    count = max(count, 1 + _getLongestPath(matrix, m, n, i+1, j, mem))

                mem[i][j] = count

                return count

        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        mem = [[0]*n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                res = max(res, _getLongestPath(matrix, m, n, i, j, mem))
        
        return res

    # directed graph + BFS, TLE
    def longestIncreasingPath2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        graph = {}
        for i in range(m):
            for j in range(n):
                this = matrix[i][j]
                dst = []
                # add left
                if j > 0 and matrix[i][j-1] > this:
                    dst.append(i*n + j-1)
                # add right
                if j < n-1 and matrix[i][j+1] > this:
                    dst.append(i*n + j+1)
                # add top
                if i > 0 and matrix[i-1][j] > this:
                    dst.append((i-1)*n + j)
                # add below
                if i < m-1 and matrix[i+1][j] > this:
                    dst.append((i+1)*n + j)
                # edges list
                graph[i*n+j] = dst

        q = deque()
        q.extend(graph.keys())
        path = 0

        while q:
            path += 1
            for i in range(len(q)):
                src = q.popleft()
                q.extend(graph[src])
        
        return path

nums = [[1]]
obj = Solution()
print(obj.longestIncreasingPath(nums))