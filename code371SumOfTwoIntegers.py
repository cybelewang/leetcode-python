"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""
class Solution:
    # python is not good to solve this problem
    # https://www.hrwhisper.me/leetcode-sum-two-integers/
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MOD     = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            a, b = (a ^ b) & MOD, ((a & b) << 1) & MOD
        return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT
    
test_cases = [(1, 2), (-1, 0), (-1, 1)]
obj = Solution()
for a, b in test_cases:
    print(str(a) + '+' + str(b) + ' = ' + str(obj.getSum(a,b)))