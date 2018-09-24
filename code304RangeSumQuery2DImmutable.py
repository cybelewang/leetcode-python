"""
304 Range Sum Query 2D - Immutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""
# update each cell to be the sum of all top-left cells (include itself)
class NumMatrix:
    
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """                
        self.matrix = matrix

        if len(matrix) < 1 or len(matrix[0]) < 1:
            m, n = 0, 0
        else:
            m, n = len(matrix), len(matrix[0])
            
        for i in range(1, m):
            self.matrix[i][0] += self.matrix[i-1][0]

        for j in range(1, n):
            self.matrix[0][j] += self.matrix[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                self.matrix[i][j] += self.matrix[i-1][j] + self.matrix[i][j-1] - self.matrix[i-1][j-1]        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # what to return if row1, col1, row2, col2 invalid?
        if row1 < 0 or row2 >= len(self.matrix) or col1 < 0 or col2 >= len(self.matrix[0]):
            return 0

        res = self.matrix[row2][col2]
        if col1 > 0:
            res -= self.matrix[row2][col1-1]
        if row1 > 0:
            res -= self.matrix[row1-1][col2]
        if row1 > 0 and col1 > 0:
            res += self.matrix[row1-1][col1-1]

        return res


# Your NumMatrix object will be instantiated and called as such:
matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))# -> 8
print(obj.sumRegion(1, 1, 2, 2))# -> 11
print(obj.sumRegion(1, 2, 2, 4))# -> 12

