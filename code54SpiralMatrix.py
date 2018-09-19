"""
54 Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
# similar problems: 48 Rotate Image
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix) < 1:
            return []

        offset = 0
        m, n = len(matrix), len(matrix[0])
        res = []
        while m > 1 and n > 1:
            for j in range(n-1):
                res.append(matrix[offset][offset + j])
            for i in range(m-1):
                res.append(matrix[offset + i][offset + n - 1])
            for j in range(n-1):
                res.append(matrix[offset + m - 1][offset + n - 1 - j])
            for i in range(m-1):
                res.append(matrix[offset + m - 1 - i][offset])
            offset += 1
            m -= 2
            n -= 2

        if m == 1:
            for j in range(n):
                res.append(matrix[offset][offset + j])
        elif n == 1:    # trap here: don't use if n==1, otherwise [[1]] may result [1, 1]
            for i in range(m):
                res.append(matrix[offset + i][offset])

        return res

obj = Solution()
test_case = [[1],[2]]
print(obj.spiralOrder(test_case))