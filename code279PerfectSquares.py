"""
279 Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
# pitfall: think the largest m (m*m <= n) will get the least number
from math import sqrt, floor
from collections import deque
class Solution:
    # BFS solution, https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = []
        for x in range(1, n+1):
            if x*x <= n:
                lst.append(x*x)
            else:
                break

        queue = deque()
        queue.append(n)
        level = 0
        while len(queue) > 0:
            level += 1
            N = len(queue)
            for i in range(N):                
                remain = queue.popleft()
                for square in lst:
                    if square == remain:
                        return level
                    elif square < remain:
                        queue.append(remain - square)
                    else:
                        break
        
        return level


    # DP solution, TLE
    def numSquares2(self, n):
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

    # Recursive solution, TLE
    def numSquares3(self, n):
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


test_cases = [1, 2, 3, 4, 7, 12, 13, 15, 16]
obj = Solution()
for case in test_cases:
    print(case, end = '->')
    print(obj.numSquares(case))