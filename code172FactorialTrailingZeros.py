"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""
# Each '5' in the i <= n contributes to a '0'
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
