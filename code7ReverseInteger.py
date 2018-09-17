"""
7 Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
# Better to solve this in C++ because it has 32 bit integer. Python will automatically extend the integer to 64 bit.
# If overflow happens, the back calculation will not get the same result
# For example: a = b*10 + c, where c < 10. If overflow happens, a/10 != b

# Reverse a signed 32 bit integer. 
# For example, 123 should return 321, -1234 should return -4321. 
# For overflowed result, return 0

def reverseInteger(num):    
    """
    :type num: int
    :rtype: int
    """
    # original solution
    MAX_POS_INT = 2**31 - 1
    MAX_NEG_INT = 2**31
    Is_Negative = False
    allowance = MAX_POS_INT
    if num < 0:
        Is_Negative = True
        allowance = MAX_NEG_INT
        num *= -1
    # push digits to stack
    stack = []
    while num != 0:
        stack.append(num % 10)
        num //= 10
    # pop digits from stack
    result = 0
    i = 0   # power to 10    
    while stack:
        digit = stack.pop()
        increment = digit*(10**i)
        allowance -= increment
        if allowance >= 0:
            result += increment
            i = i + 1
        else:
            return 0
    
    if Is_Negative:
        result *= -1
    
    return result


test_case = [0, 123, -123, 2147483647, 2147483641, -2147483648, 123456789, -12345678]

for num in test_case:
    print(reverseInteger(num))