"""
378 Kth Smallest Element in a Sorted Matrix

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
# similar problems: 373 Find K Pairs With Smallest Sums; 668 Kth Smallest Number in Multiplication Table
from heapq import *
class Solution:
    def kthSmallest3(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def search(matrix, target):
            """
            count elements <= target in matrix
            """
            n = len(matrix)
            i, j, res = n-1, 0, 0
            while i > -1 and j < n:
                if matrix[i][j] <= target:
                    # matrix[0][j] to matrix[i][j] are all <= target
                    res += i + 1
                    j += 1
                else:
                    i -= 1
            return res
        
        # main
        # binary search
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right)//2
            cnt = search(matrix, mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        
        return left

    # binary search solution
    # https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])

        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            mid = (low + high)//2
            count, j = 0, n - 1
            for i in range(m):
                while j >=0 and matrix[i][j] > mid:
                    j -= 1
                count += j + 1
            
            if count < k:
                low = mid + 1
            else:
                high = mid
        
        return low
        
    # min heap, key is that when we select a cell matrix[x][y], the next smallest must be in [x+1][y] or [x][y+1]
    # this is similar to 355 design twitter's get latest news, or 23 merge k sorted lists, the only difference is that this problem needs to push two neighbors after popping out one.
    # https://stackoverflow.com/questions/15179536/kth-smallest-element-in-sorted-matrix
    """
    O(k log(k)) solution.
    Build a minheap.
    Add (0,0) to the heap. While, we haven't found the kth smallest element, remove the top element (x,y) from heap and add next two elements [(x+1,y) and (x,y+1)] if they haven't been visited before.
    We are doing O(k) operations on a heap of size O(k) and hence the complexity.
    """
    def kthSmallest2(self, matrix, k):
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