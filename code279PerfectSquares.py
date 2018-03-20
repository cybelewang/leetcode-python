"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
# pitfall: think the largest m (m*m <= n) will get the least number
from math import sqrt, floor
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        f = [i for i in range(n+1)]
        for i in range(4, n+1):
            M = floor(sqrt(i))            
            for m in range(1, M+1): # need to go through all sub squres to get the least number
                f[i] = min(f[i], 1 + f[i - m*m])
        
        return f[n]


test_cases = [1, 2, 3, 4, 7, 12, 13, 15, 16]
obj = Solution()
for case in test_cases:
    print(case, end = '->')
    print(obj.numSquares(case))