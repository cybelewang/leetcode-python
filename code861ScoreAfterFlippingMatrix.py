"""
861 Score After Flipping Matrix

We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

 

Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.
"""
class Solution:
    # my own solution
    # for each row, make the first element 1
    # then for each column, count 1 and 0, and add the most with weight   
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        # for each row, make the first element 1
        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] ^= 1

        # now for each column, count 1 and 0, and add the most    
        res, factor = 0, 2**(n-1)
        for j in range(n):
            count1 = 0
            for i in range(m):
                if A[i][j]:
                    count1 += 1
            
            count1 = max(count1, m-count1)
            res += count1*factor
            factor //= 2
        
        return res

A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(Solution().matrixScore(A))