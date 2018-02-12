"""
Given an integer, write a function to determine if it is a power of two.
"""
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n < 1 else n & (n-1)==0

obj = Solution()
test_cases = [1, 2, 3, 4, 5, 6, 8, 10]
for case in test_cases:
    print(case, end = ' -> ')
    print(obj.isPowerOfTwo(case))