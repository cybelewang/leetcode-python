"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
from math import sqrt, floor
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        m = floor(sqrt(n))
        res = 2**31-1
        for i in range(1, m + 1):
            res = min(res, 1 + self.numSquares(n - i**2))
        
        return res


test_cases = [1, 2, 4, 7, 12, 13, 15, 16]
obj = Solution()
for case in test_cases:
    print(case, end = '->')
    print(obj.numSquares(case))