"""
201 Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""
# The difference (in binary form) between n and m will show how many bits flipped
# For example, 7 - 5 = 2, in binary form it is 10, which means the right most two bits will flip
# So we should create a number 1111111111111111111111111111111100 as a mask "AND" with m and n
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
        
        # (1<<order) - 1 making right side all 0s (length = order), and left side all 1s (length = 32-order)
        return m & ~((1<<order) - 1) & n

m, n = 5, 7
obj = Solution()
print(obj.rangeBitwiseAnd(m, n))