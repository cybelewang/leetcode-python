"""
74 Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        # step 1: search the row by searching the row head element
        i, j, row = 0, len(matrix) - 1, 0   # bug fixed: j should be len
        while i <= j:
            row = (i + j)//2
            if matrix[row][0] == target:
                return True
            elif matrix[row][0] > target:
                j = row - 1
            else:
                i = row + 1
        
        # After exiting the while loop, i will be the correct "insert" row index, so target must be in row i-1
        if i == 0:
            return False
        else:
            row = i - 1
        
        # step 2: search all elements in that row
        i, j, col = 0, len(matrix[0]) - 1, 0
        while i <= j:
            col = (i + j)//2
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                j = col - 1
            else:
                i = col + 1
        
        # Not found
        return False

# 2nd round solution on 9/19/2018
# 1st binary search on 1st column
# 2nd binary search on the possible row
class Solution2:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m < 1:   return False
        n = len(matrix[0])

        top, bottom = 0, m
        while top < bottom:
            mid = (top + bottom)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                bottom = mid
            else:
                top = mid + 1
        
        if bottom == 0:
            return False
        
        left, right = 0, n
        while left < right:
            mid = (left + right)//2
            if matrix[bottom-1][mid] == target:
                return True
            elif matrix[bottom-1][mid] < target:
                left = mid + 1
            else:
                right = mid

        return False

test_matrix = [[1,3,5,7],[10, 11, 16, 20], [23, 30, 34, 50]]
obj = Solution2()
print(obj.searchMatrix(test_matrix, 50))




        