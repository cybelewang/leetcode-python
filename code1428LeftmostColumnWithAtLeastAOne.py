"""
1428 Leftmost Column with at Least a One

(This problem is an interactive problem.)
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.
Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.
You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:
BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.
For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.
 
Example 1:
Input: mat = [[0,0],[1,1]]
Output: 0

Example 2:
Input: mat = [[0,0],[0,1]]
Output: 1

Example 3:
Input: mat = [[0,0],[0,0]]
Output: -1

Example 4:
Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
 
Constraints:
rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.
"""
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    # Best solution, O(N+M)
    # search from top right to bottom left, when seeing 1, search left, when seeing 0, search next row
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        row, col = 0, n-1

        while row < m and col > -1:
            if binaryMatrix.get(row, col):
                col -= 1
            else:
                row += 1
        
        return col+1 if col < (n -1) else -1

    # binary search solution, restricting each row's search range. O(M*logN)
    def leftMostColumnWithOne2(self, binaryMatrix: 'BinaryMatrix') -> int:
        def binarysearch(bm, row, colEnd):
            # binary search to find the most left column index in row "row"
            # call this function only when we know 1 exists before colEnd on row "row"
            left, right = 0, colEnd
            while left < right:
                mid = (left + right)//2
                if bm.get(row, mid):
                    right = mid
                else:
                    left = mid + 1
            return right
        
        m, n = binaryMatrix.dimensions()
        bFoundOne = False # think about [[0], [0]], we want to return -1
        for row in range(m):
            if binaryMatrix.get(row, n-1):
                n = binarysearch(binaryMatrix, row, n) + 1
                bFoundOne = True

        return n-1 if bFoundOne else -1