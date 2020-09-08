"""
29 Divide Two Integers

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""
from math import *
def divide(self, dividend, divisor):
    # handle sign
    sign = 1
    if dividend == 0: return 0
    if dividend > 0 and divisor < 0:
        divisor, sign = -divisor, -1
    elif dividend < 0 and divisor > 0:
        dividend, sign = -dividend, -1
    elif dividend < 0 and divisor < 0:
        dividend, divisor = -dividend, -divisor        
    
    def helper(num, div):
        if num < div: return 0
        res = 1
        d = div
        while d + d <= num:
            d = d + d
            res = res + res
        return res + helper(num - d, div)
    
    ans = helper(dividend, divisor)
    if sign > 0:
        return min(ans, 2**31 - 1)
    else:
        return -2**31 if ans > 2**31 else -ans

def divide2(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if (dividend == 0):
        return 0
    elif divisor == 0:
        return 2**31 - 1
    else:
        isNegative = False
        if dividend < 0 and divisor > 0:
            isNegative = True
        elif dividend > 0 and divisor < 0:
            isNegative = True
        else:
            isNegative = False
        
        result = int(pow(2, (log(abs(dividend), 2) - log(abs(divisor), 2))))

        if (False == isNegative) and result > (2**31 - 1):
            return 2**31 - 1
        elif isNegative and result > 2**31:
            return -(2**31)

        if isNegative:
            result = 0 - result
        
    return result

test_cases = [(0, 0), (0, 1), (1, 0), (1, 1), (3, 5), (3, -2), (-6, -2), (2**33, 1), (-2147483648, -1),(2147483647, 1)]
for (x, y) in test_cases:
    print(divide(x, y), end='\n')
    #(0, 0), (0, 1), (1, 0), (1, 1), (3, 5), (3, -2), (-6, -2), (2**33, 1), (-2147483648, -1), 