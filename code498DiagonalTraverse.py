"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:
The total number of elements of the given matrix will not exceed 10,000.
"""
class Solution:
    # my own solution
    # in general the row index + col index will increase from 0 to M + N - 2
    # clock-wise turn: hit either the top row (increase col), or the right col (increase row)
    # counter-clock-wise turn: hit either the left col (increase row), or the bottom row (increase col)
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        M  = len(matrix)
        if M == 0: return res
        N = len(matrix[0])

        i, j, clock_wise = 0, 0, True
        res.append(matrix[0][0])
        for _ in range(M + N - 1):
            if clock_wise:  # clock-wise turn
                if j + 1 < N:   # hit top row, increase col
                    j += 1
                else:   # hit right col, increase row
                    i += 1
                # loop until hit the bottom row or left col
                while i < M and j > -1:
                    res.append(matrix[i][j])
                    i += 1
                    j -= 1
                # restore i, j to valid values
                i -= 1
                j += 1
            else:
                if i + 1 < M:
                    i += 1
                else:
                    j += 1
                while j < N and i > -1:
                    res.append(matrix[i][j])
                    j += 1
                    i -= 1
                # restore i, j to valid values
                i += 1
                j -= 1
            
            clock_wise = not clock_wise

        return res

matrix = [ [ 1, 2, 3, 0 ], [ 4, 5, 6, 0 ], [ 7, 8, 9, 0 ]]
print(Solution().findDiagonalOrder(matrix))