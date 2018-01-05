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
        #res = str(sign * (numerator//denominator))  # bug fixed: this is old expression str(sign * (numerator//denominator)), but for 0, it won't generate -0, cases are -1/2, 0/-2
        div = numerator//denominator
        remain = numerator % denominator

        if div == 0 and remain == 0:
            return '0'
        else:
            res = str(div)
            if sign < 0:
                res = '-' + res

        if remain == 0:
            return res
        else:
            res += '.'

        div_list = []
        history = set()
        while remain > 0:
            if remain in history:
                return res + '(' + ''.join(map(str, div_list)) + ')'
            else:
                history.add(remain)
                remain *= 10
                div_list.append(remain//denominator)
                remain %= denominator

        return res + ''.join(map(str, div_list))

test_cases = [(0, 1), (50, 13), (1, 3), (1, 2), (2, -3), (-1, 2), (1, -3), (0, -2)]
obj = Solution()
for case in test_cases:
    print(obj.fractionToDecimal(case[0], case[1]))