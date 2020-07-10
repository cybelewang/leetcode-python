"""
221 Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""
# similar problems: 84 Largest Rectangle in Histogram, 85 Maximal Rectangle
# DP, assume dp[i][j] is the max square's size with (i, j) as bottom right corner, then dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
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

    # 2nd round solution on 2/20/2019, using 1D dp array
    def maximalSquare2(self, matrix):
        m = len(matrix)
        if m < 1:   return 0
        n = len(matrix[0])
        if n < 1:   return 0
        
        maxSize = 0
        dp = [0]*n
        for i in range(m):
            pre = 0 # temporarily save dp[0] as pre for dp[1] use, pre is like dp[i-1][j-1]
            dp[0] = 1 if matrix[i][0] == '1' else 0 # handle dp[0] specially
            maxSize = max(maxSize, dp[0]) # update result
            for j in range(1, n):
                temp = dp[j]    # temporarily save dp[j] before it gets updated
                if matrix[i][j] == '1':
                    dp[j] = min(pre, dp[j-1], dp[j]) + 1
                    maxSize = max(maxSize, dp[j]) # update result
                else:
                    dp[j] = 0
                pre = temp  # assign temp to pre for next j loop use
        
        return maxSize*maxSize

obj = Solution()
#test_matrix = [['1', '0', '1', '0', '0'],['1', '0', '1', '1', '1'],['1', '1', '1', '1', '1'],['1', '0', '0', '1', '0']]
#test_matrix = [["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]
#test_matrix = [['1']]
test_matrix = [["0"]]
print(obj.maximalSquare2(test_matrix))