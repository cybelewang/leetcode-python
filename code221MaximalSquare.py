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

        #if m == 1 or n == 1:   # bug here, for example [['0']]
        #    return 1

        # previous row element's height in a single column (i.e., number of continuous '1's in a single column)
        prevH = [0]*n

        # a bug here, trying to use 1-D array
        # prevN = [0]*(n+1)
        # correct solution is using a 2D to store the max square size
        N = [[0 for j in range(n)] for i in range(m)]

        res = 0
        for i in range(m):
            prevW = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    if i > 0 and j > 0:
                        N[i][j] = min(N[i-1][j-1], prevH[j], prevW) + 1
                    else:
                        N[i][j] = 1
                    res = max(res, N[i][j]**2)
                    prevW += 1
                    prevH[j] += 1                    
                else:
                    prevW = 0
                    prevH[j] = 0
                    N[i][j] = 0

        return res

obj = Solution()
#test_matrix = [['1', '0', '1', '0', '0'],['1', '0', '1', '1', '1'],['1', '1', '1', '1', '1'],['1', '0', '0', '1', '0']]
#test_matrix = [["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]] # bug here
test_matrix = [['1']]
print(obj.maximalSquare(test_matrix))