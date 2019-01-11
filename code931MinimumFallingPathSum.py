"""
931 Minimum Falling Path Sum

Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.

Note:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
"""
# similar problems: 120 Triangle
class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n, ans = len(A), len(A[0]), 2**31-1
        if m == 1:  # bug fixed: corner case when len(A)==1
            return min(A[0])
        for i in range(1, m):
            for j in range(n):
                lo, hi = max(0, j-1), min(j+2, n)
                A[i][j] += min(A[i-1][lo:hi])
                if i == m - 1:
                    ans = min(ans, A[i][j])
        
        return ans
    def minFallingPathSum_OJ(self, A):
        while len(A) >= 2:
            row = A.pop()            
            for i in xrange(len(row)):
                A[-1][i] += min(row[max(0,i-1): min(len(row), i+2)])
        return min(A[0])

A = [[1,2,3],[4,5,6],[7,8,9]]
#A = [[2, 1, -3], [-10, 10, 7], [-1, 10, -4]]
print(Solution().minFallingPathSum(A))