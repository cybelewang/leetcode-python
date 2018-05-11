"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
# zip takes the shortest, and itertools.zip_longest takes the longest input and optional fillvalue
from itertools import zip_longest
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # check '' + '', '' + '1'
        base, carry, digits = ord('0'), 0, []
        for x, y in zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            add_res = ord(x) + ord(y) - 2*base + carry
            digits.append(chr(add_res%10 + base))
            carry = add_res//10
        
        digits.append(chr(carry + base))

        return ''.join(digits[::-1]).lstrip('0') or '0'

obj = Solution()
print(obj.addStrings('123', '4567'))

