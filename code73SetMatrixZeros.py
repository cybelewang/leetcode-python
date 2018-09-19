"""
73 Set Matrix Zeros

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
        
        # Check if first row and first column has zero
        rowHasZero, colHasZero = False, False
        m, n = len(matrix), len(matrix[0])

        for j in range(n):
            if matrix[0][j] == 0:
                rowHasZero = True
                break
        
        for i in range(m):
            if matrix[i][0] == 0:
                colHasZero = True
                break
        # Iterate the rest of the matrix (not the first row and first column), set the row and column head to zero if [i][j] is zero
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):   # bug fixed here: we should not set the first row and first column because they are "marks". We should set them at last.  
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        # set the first row and first column in last step
        if colHasZero:
            for i in range(m):
                matrix[i][0] = 0
        if rowHasZero:
            for j in range(n):
                matrix[0][j] = 0

# 2nd round solution on 9/19/2018
class Solution2:
    def setZeroes(self, matrix):
        m = len(matrix)
        if m < 1:   return
        n = len(matrix[0])

        firstRowZero = any(matrix[0][j] == 0 for j in range(n)) # mark if any 0s in the first row
        firstColZero = any(matrix[i][0] == 0 for i in range(m)) # mark if any 0s in the first column

        # iterate matrix except the 1st row and 1st column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0    # set the row head to 0
                    matrix[0][j] = 0    # set the column head to 0
        
        # set entire row to 0 if the row head is 0, except the 1st row
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        # set entire column to 0 if the column head is 0, except the 1st column
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        # now process the 1st row
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0

        # now process the 1st column
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0


test_case = [[1,1,1],[0,1,2]]
obj = Solution2()
obj.setZeroes(test_case)
print(test_case)
