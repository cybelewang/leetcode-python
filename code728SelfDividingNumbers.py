"""
728 Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
"""
from operator import mul
from functools import reduce
class Solution:
    # another brutal force solution by checking if all digits can be divided
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right+1):
            digits = [int(c) for c in str(num)] # array of digits
            if all(digits) and all(map(lambda d: num % d == 0, digits)):
                res.append(num)

        return res
    # my own solution using least common multiple
    def selfDividingNumbers2(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right+1):
            digits = [int(c) for c in str(num)] # array of digits
            if digits.count(0) > 0: continue    # excludes numbers with 0
            lcm = reduce(mul, digits)//reduce(self.gcd, digits) # least common multiple
            if num % lcm == 0:
                res.append(num)
        
        return res

    def gcd(self, x, y):    # greatest common divisor
        return x if y == 0 else self.gcd(y, x%y)

print(Solution().selfDividingNumbers(1, 22))