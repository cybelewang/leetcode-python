"""
308. Range Sum Query 2D - Mutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

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
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10

Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""
"""
Similar problem: 304 Range Sum Query 2D - Immutable
Use Binary Index Tree (BIT) to quickly get the sum of the rectangle area from (0, 0) to (row, col), inclusive
"""
import unittest
class NumMatrix:

    def __init__(self, matrix):
        self.M = len(matrix)
        self.N = len(matrix[0]) if self.M > 0 else 0
        self.mat = [[0]*self.N for _ in range(self.M)] # (M)*(N) matrix that stores current value (update method may change value)
        self.bit = [[0]*(self.N+1) for _ in range(self.M+1)] # (M+1)*(N+1) matrix that represents a 2-D BIT
        # use update method to create the 2-D BIT
        for i in range(self.M):
            for j in range(self.N):
                self.update(i, j, matrix[i][j])
        
    def update(self, row: int, col: int, val: int) -> None:
        if -1 < row < self.M and -1 < col < self.N:
            diff = val - self.mat[row][col]
            self.mat[row][col] = val 
            i = row + 1 # mat has 0-based index and BIT has 1-based index. Pitfall: don't initialize j to (col + 1) here
            while i < self.M + 1:
                j = col + 1
                while j < self.N + 1:
                    self.bit[i][j] += diff
                    j += j & (-j)
                i += i & (-i)

    def getSum(self, row: int, col: int) -> int:
        """
        sum of the rectangle area from (0, 0) to (row, col), exclusive row & col
        """
        res = 0
        if -1 < row - 1 < self.M and -1 < col - 1 < self.N:
            i = row
            while i > 0:
                j = col
                while j > 0:
                    res += self.bit[i][j]
                    j -= j & (-j)
                i -= i & (-i)
        return res

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.getSum(row2+1, col2+1)\
             - self.getSum(row2+1, col1)\
             - self.getSum(row1, col2+1)\
             + self.getSum(row1, col1)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

class Test(unittest.TestCase):
    def test_1(self):
        matrix = [[3, 0, 1, 4, 2],\
            [5, 6, 3, 2, 1],\
            [1, 2, 0, 1, 5],\
            [4, 1, 0, 1, 7],\
            [1, 0, 3, 0, 5]]
        #matrix = [[3, 0], [5, 6]]
        m = NumMatrix(matrix)
        self.assertEqual(14, m.getSum(2, 2))
        self.assertEqual(8, m.sumRegion(2, 1, 4, 3))
        m.update(3, 2, 2)
        self.assertEqual(10, m.sumRegion(2, 1, 4, 3))

if __name__ == "__main__":
    unittest.main(exit = False)