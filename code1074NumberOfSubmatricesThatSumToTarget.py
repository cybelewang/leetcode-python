"""
1074 Number of Submatrices That Sum to Target

Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
 

Note:

1 <= matrix.length <= 300
1 <= matrix[0].length <= 300
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
"""
from collections import defaultdict
class Solution:
    # https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
    # reduce to 1-D problem (560) by fixing column
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        R, C = len(matrix), len(matrix[0])
        ps = [[0]*(C+1) for _ in range(R+1)]
        for r in range(1, R+1):
            for c in range(1, C+1):
                ps[r][c] = matrix[r-1][c-1] + ps[r][c-1] + ps[r-1][c] - ps[r-1][c-1]
        
        count = 0
        for r1 in range(1, R+1):
            for r2 in range(r1, R+1):
                h = defaultdict(int)
                h[0] = 1
                
                for c in range(1, C+1):
                    su = ps[r2][c] - ps[r1-1][c]
                    count += h[su-target]
                    h[su] += 1
        
        return count