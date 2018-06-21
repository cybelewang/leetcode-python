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
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        M  = len(matrix)
        if M == 0: return res
        N = len(matrix[0])

        i, j, up = 0, 0, True
        for sum_ in range(M + N - 1):
            if up:
                i = sum_ - j
                while j <= sum_:
                    res.append(matrix[i][j])
                    j += 1
                    i -= 1
            else:
                j = sum_ - i
                while i >= 0:
                    res.append(matrix[i][j])
                    i -= 1
                    j += 1
            
            up = not up

        return res