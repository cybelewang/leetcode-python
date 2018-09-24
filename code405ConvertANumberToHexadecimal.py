"""
405 Convert a Number to Hexadecimal

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"
"""
class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # two's complement
        if num < 0:
            num += 2**32

        res = ''
        while num:
            d = num%16
            if d < 10:
                res = chr(d + ord('0')) + res
            else:
                res = chr(d - 10 + ord('a')) + res
            num //= 16
        
        return res or '0'

test_cases = [0, 26, -1]
obj = Solution()
for num in test_cases:
    print(obj.toHex(num))
