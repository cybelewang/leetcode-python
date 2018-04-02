"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3**19%n == 0   # 3**19 is the max power of three within 2**31