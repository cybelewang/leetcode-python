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

        s = floor(sqrt(n))
        N = s**2
        num = n//N

        return num + self.numSquares(n - num*N)

test_cases = [1, 2, 12, 13]
obj = Solution()
for case in test_cases:
    print(case, end = '->')
    print(obj.numSquares(case))