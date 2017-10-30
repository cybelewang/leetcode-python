"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
"""
# Use dynamic programming 
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        maxArea = 0

        # Use a tuple (width, height) to save the maximum width and maximum height with [i][j] as the right bottom point
        if matrix[0][0] == '1':
            matrix[0][0] = (1, 1)   # max width 1, max height 1
            maxArea = 1 # bug fixed here: forgot to update maxArea when m and n are 1
        else:
            matrix[0][0] = (0, 0)   # max width 0, max height 0

        # Process the top row
        for j in range(1, n):
            if matrix[0][j] == '1':
                matrix[0][j] = (matrix[0][j-1][0] + 1, 1)
                maxArea = max(matrix[0][j][0], maxArea)
            else:
                matrix[0][j] = (0, 0)
        
        # Process the left column
        for i in range(1, m):
            if matrix[i][0] == '1':
                matrix[i][0] = (1, matrix[i-1][0][1] + 1)
                maxArea = max(matrix[i][0][1], maxArea)
            else:
                matrix[i][0] = (0, 0)
        
        # Now process the rest of the matrix
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':                    
                    recArea = (min(matrix[i-1][j-1][0], matrix[i][j-1][0]) + 1)*(min(matrix[i-1][j-1][1], matrix[i-1][j][1]) + 1)   # possible rectangle rectangle area
                    rowArea = matrix[i][j-1][0] + 1 # possible row-like rectange area
                    colArea = matrix[i-1][j][1] + 1 # possible column-like rectange area

                    maxArea = max(maxArea, recArea, rowArea, colArea)
                    matrix[i][j] = (rowArea, colArea)
                else:
                    matrix[i][j] = (0, 0)

        return maxArea 

obj = Solution()
test_matrix = [
    ['1','0','1','0','0'],
    ['1','0','1','1','1'],
    ['1','1','1','1','1'],
    ['1','0','0','1','0']
]
print(obj.maximalRectangle(test_matrix))