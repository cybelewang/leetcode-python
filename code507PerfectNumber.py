"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)

"""
from math import sqrt
class Solution:
    # cheating solution
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in (6, 28, 496, 8128, 33550336)

    def checkPerfectNumber2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return False
        sum_ = 1
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:    # if num can be divided by i, then num can be divided by num//i too
                sum_ += (i + num//i)
            if i**2 == num: # if num is a square, we have added i twice, so we need to reduce i in this case
                sum_ -= i
            if sum_ > num:
                return False

        return sum_ == num

print(Solution().checkPerfectNumber2(8128))