"""
504 Base 7

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].

"""
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        is_negative = num < 0
        if is_negative:
            num *= -1
        digits = []
        while num:
            digits.append(str(num%7))
            num //= 7
        
        if is_negative:
            digits.append('-')
        
        return ''.join(digits[::-1]) or '0'

print(Solution().convertToBase7(-1000000))