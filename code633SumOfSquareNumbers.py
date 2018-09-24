"""
633 Sum of Square Numbers

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a^2 + b^2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
"""
from math import sqrt
class Solution:
    # two pointers from http://www.cnblogs.com/grandyang/p/7190506.html
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a, b = 0, int(sqrt(c)) + 1
        while a <= b:
            sum_ = a**2 + b**2
            if sum_ == c:
                return True
            elif sum_ < c:
                a += 1
            else:
                b -= 1
        
        return False

    # my own solution, iterate a from 0 to sqrt(c), find if c - a^2 is a square
    def judgeSquareSum2(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def isSquare(num):
            if num < 0:
                return False
            return (int(sqrt(num)))**2 == num

        for i in range(int(sqrt(c//2))+1):
            a2 = i**2
            b2 = c - a2
            if isSquare(b2):
                return True

        return False

test_cases = [0, 1, 2, 3, 5, 9, 15, 17, 2**31-1]
obj = Solution()

for num in test_cases:
    print(num, end = ' -> ')
    print(obj.judgeSquareSum(num))