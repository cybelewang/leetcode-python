"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # corner cases
        m = len(matrix)
        if m < 1:
            return 0
        n = len(matrix[0])
        if n < 1:
            return 0

        if m == 1 or n == 1:
            return 1

        # previous row element's height in a single column (i.e., number of continuous '1's in a single column)
        prevH = [0]*n

        # previous row element's square size (i.e., the size of square with the element as the bottom right point)
        prevN = [0]*n

        res = 0
        for i in range(m):
            prevW = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    prevN[j] = min(prevN[j], prevH[j], prevW) + 1
                    res = max(res, prevN[j]**2)
                    prevW += 1
                    prevH[j] += 1                    
                else:
                    prevW = 0
                    prevH[j] = 0
                    prevN[j] = 0

        return res

obj = Solution()
#test_matrix = [['1', '0', '1', '0', '0'],['1', '0', '1', '1', '1'],['1', '1', '1', '1', '1'],['1', '0', '0', '1', '0']]
test_matrix = [['1','0'], ['1', '1']]
print(obj.maximalSquare(test_matrix))