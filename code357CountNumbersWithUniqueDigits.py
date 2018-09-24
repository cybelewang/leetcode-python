"""
357 Count Numbers with Unique Digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
"""
class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851, 5611771, 8877691]

        return res[n] if n < 11 else res[10]

    def countNumbersWithUniqueDigits2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n == 1:
            return 10
        elif n > 10:
            n = 10

        withoutZeros, withZeros = [0]*(n+1), [0]*(n+1)  # index is the length of number, value is the number of unique digits
        withoutZeros[1] = 9 # 1 to 9
        withZeros[1] = 1    # 0

        for i in range(2, n+1):
            withoutZeros[i] = (10-i)*withoutZeros[i-1] if i < 10 else 0 # by adding 9-(i-1) kinds of digits to the highest digit
            withZeros[i] = (i-1)*withoutZeros[i-1]  # by inserting 0
        
        return sum(withoutZeros) + sum(withZeros)

obj = Solution()
for n in range(11):
    print(obj.countNumbersWithUniqueDigits(n))    
