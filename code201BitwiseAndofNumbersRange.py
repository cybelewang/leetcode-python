"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n:
            return m

        d, order = n - m, 0 # order is the position of highest '1' of d
        while d > 0:
            d = d >> 1
            order += 1
        
        return m & ~((1<<order) - 1) & n

m, n = 5, 7
obj = Solution()
print(obj.rangeBitwiseAnd(m, n))