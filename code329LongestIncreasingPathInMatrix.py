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
    # directed graph + BFS
    def longestIncreasingPath(self, matrix):
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
                encode = i*n + j
                this = matrix[i][j]
                # add left
                if j > 0 and matrix[i][j-1] > this:
                    graph[encode] = graph.get(encode, []).append(i*n + j-1)
                # add right
                if j < n-1 and matrix[i][j+1] > this:
                    graph[encode] = graph.get(encode, []).append(i*n + j+1)
                # add top
                if i > 0 and matrix[i-1][j] > this:
                    graph[encode] = graph.get(encode, []).append((i-1)*n + j)
                # add below
                if i < m-1 and matrix[i+1][j] > this:
                    graph[encode] = graph.get(encode, []).append((i+1)*n + j)

        q = deque()
        q.extend(graph.keys())
        path = 0

        while q:
            path += 1
            for i in range(len(q)):
                src = q.popleft()
                q.extend(graph[src])
        
        return path

nums = [[3,4,5], [3,2,6], [2,2,1]]
obj = Solution()
print(obj.longestIncreasingPath(nums))