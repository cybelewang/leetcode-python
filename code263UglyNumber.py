"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""
class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        while num > 1 and num % 5 == 0:
            num //= 5
        
        while num > 1 and num % 3 == 0:
            num //= 3

        while num > 1 and num % 2 == 0:
            num //= 2

        return num == 1

obj = Solution()
for i in range(-1,21):
    print(i, end = ', ')
    print(obj.isUgly(i))

