"""
867 Transpose Matrix

Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(A), len(A[0])
        B = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                B[i][j] = A[j][i]

        return B

    # my own solution by trying different size matrix
    def transpose_Wrong(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(i, n):
                x = min(m-1, j)
                y = i + j - x
                A[i][j], A[x][y] = A[x][y], A[i][j]

        return A

A = [[1,2,3,4]]
print(Solution().transpose(A))