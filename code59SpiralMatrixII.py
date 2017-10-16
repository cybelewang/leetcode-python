"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return []

        res = [[0 for j in range(n)] for i in range(n)]
        k, m = 1, n
        for offset in range((n+1)//2):
            if m == 1:
                res[offset][offset] = k
            else:
                # top
                for i in range(m - 1):
                    res[offset][offset + i] = k
                    k += 1
                # right
                for i in range(m - 1):
                    res[offset + i][offset + m - 1] = k
                    k += 1
                # bottom
                for i in range(m - 1):
                    res[offset + m - 1][offset + m - 1 - i] = k
                    k += 1
                # left
                for i in range(m - 1):
                    res[offset + m - 1 - i][offset] = k
                    k += 1

            m -= 2
        
        return res

obj = Solution()
print(obj.generateMatrix(4))

            