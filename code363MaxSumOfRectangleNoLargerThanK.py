"""
363 Max Sum of Rectangle No Larger Than K

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
"""
from bisect import bisect_left, insort_left
class Solution:
    # http://www.cnblogs.com/grandyang/p/5617660.html
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n, res = len(matrix), len(matrix[0]), -2**31
        for i in range(n):
            sum = [0]*m
            for j in range(i, n):
                for p in range(m):
                    sum[p] += matrix[p][j]
                
                curSum, curMax = 0, -2**31
                s = [0]
                for a in sum:
                    curSum += a
                    index = bisect_left(s, curSum-k)
                    if index < len(s):
                        curMax = max(curMax, curSum - s[index])
                    insort_left(s, curSum)
                
                res = max(res, curMax)
        
        return res

matrix = [[3]]
obj = Solution()
print(obj.maxSumSubmatrix(matrix, 2))