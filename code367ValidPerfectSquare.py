"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""
# in math, a square will be sum of consequective odd numbers, for example:
# 1 = 1
# 4 = 1 + 3
# 9 = 1 + 3 + 5
# 16 = 1 + 3 + 5 + 7

class Solution:
    # more elegant binary search, why does this work?
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i, j = 0, num
        while i <= j:
            mid = (i + j)//2
            s = mid**2
            if s == num:
                return True
            elif s < num:
                i = mid + 1
            else:
                j = mid - 1
        
        return False

    # awkward solution using binary search
    def isPerfectSquare2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        elif num == 1:
            return True

        i, j, last = 0, num, -1
        while i <= j:
            mid_sqr = ((i + j)//2)**2
            if mid_sqr == last:
                return False
            else:
                last = mid_sqr

            if mid_sqr == num:
                return True
            elif mid_sqr < num:
                i = (i + j)//2
            else:
                j = (i + j)//2
        
        return False

test_cases = [-1, 0, 1, 2, 3, 4, 14, 16, 2**31-1]
obj = Solution()
for num in test_cases:
    print(num, end = ' -> ')
    print(obj.isPerfectSquare(num))