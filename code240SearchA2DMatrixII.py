"""
240 Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

"""
# similar problems: 74 Search a 2D Matrix

# From Java solution: treat the bottom left element as root or binary search tree
# if current < target, we search right because all above numbers < current. why not search down? because we already considered them in previous steps
# if current > target, we search up because all right number > current. why not search left? because we already considered them in previous steps
# if current == target, we find it

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m < 1:
            return False

        n = len(matrix[0])
        i, j = m-1, 0

        while i > -1 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1

        return False

obj = Solution()
matrix = [[-5]]

print(obj.searchMatrix(matrix, -5))