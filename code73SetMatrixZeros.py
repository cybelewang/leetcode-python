"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
# First mark the row head and column head to 0 if 0 is detected in that row and column. 
# Then set all elements in that row to 0 if row head is 0, and all elements in that column to 0 if column head is 0 
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        for j in range(n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

test_case = [[0]]
obj = Solution()
obj.setZeroes(test_case)
print(test_case)
