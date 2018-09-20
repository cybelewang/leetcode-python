"""
85 Maximal Rectangle, Maximum Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
"""
# Use problem 84, largest rectangle in histogram to help solve this problem
# First compress the 2d array above current row and current row into a 1d array, then use problem 84's solution
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        hist = []

        i = 0
        while i < len(heights):
            if not hist or heights[hist[-1]] <= heights[i]:
                hist.append(i)
                i += 1
            else:
                h = heights[hist.pop()]
                if not hist:
                    w = i
                else:
                    w = i - 1 - hist[-1]
                maxArea = max(h*w, maxArea)
        
        while hist:
            h = heights[hist.pop()]
            if not hist:
                w = len(heights)
            else:
                w = len(heights) - 1 - hist[-1]
            maxArea = max(h*w, maxArea)
        
        return maxArea

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        maxArea = 0

        height = []
        for j in range(n):
            if matrix[0][j] == '1':
                height.append(1)
            else:
                height.append(0) 
        maxArea = max(maxArea, self.largestRectangleArea(height))

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == '0':
                    height[j] = 0
                else:
                    height[j] += 1
            
            maxArea = max(maxArea, self.largestRectangleArea(height))

        return maxArea

# 2nd visit on 9/20/2018

obj = Solution()
test_matrix = [["0","0","0"],["0","0","0"],["1","1","1"]]
print(obj.maximalRectangle(test_matrix))