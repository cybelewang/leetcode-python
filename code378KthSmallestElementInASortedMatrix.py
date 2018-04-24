"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n^2.
"""
# min heap, key is that when we select a cell matrix[x][y], the next smallest must be in [x+1][y] or [x][y+1]
# this is similar to 355 design twitter's get latest news, or 23 merge k sorted lists, the only difference is that this problem needs to push two neighbors after popping out one.
# https://stackoverflow.com/questions/15179536/kth-smallest-element-in-sorted-matrix
"""
O(k log(k)) solution.

Build a minheap.

Add (0,0) to the heap. While, we haven't found the kth smallest element, remove the top element (x,y) from heap and add next two elements [(x+1,y) and (x,y+1)] if they haven't been visited before.

We are doing O(k) operations on a heap of size O(k) and hence the complexity.
"""
from heapq import *
class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])

        queue = [(matrix[0][0], 0, 0)]
        visited = {(0, 0),}
        count = 0

        while count < k:
            value, i, j = heappop(queue)
            if i < m - 1 and (i+1, j) not in visited:
                heappush(queue, (matrix[i+1][j], i+1, j))
                visited.add((i+1, j))
            if j < n - 1 and (i, j+1) not in visited:
                heappush(queue, (matrix[i][j+1], i, j+1))
                visited.add((i, j+1))
            count += 1
        
        return value


matrix = [[ 1,  5,  9], [10, 11, 13], [12, 13, 15]]
k = 8
obj = Solution()
print(obj.kthSmallest(matrix, k))