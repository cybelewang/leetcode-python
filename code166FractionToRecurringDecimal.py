"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # corner case : denominator is 0
        if denominator == 0:
            raise ValueError
        
        # Handle different signs
        sign = 1
        if numerator < 0:
            sign *= -1
            numerator *= -1
        
        if denominator < 0:
            sign *= -1
            denominator *= -1

        # Get integer result
        int_res = sign * (numerator//denominator)

        remain = numerator % denominator
        if remain == 0:
            return str(int_res)

        while remain > 0 
