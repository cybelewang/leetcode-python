"""
166 Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""
# pitfalls: 
# (1) num and den have different signs, python will floor down for negative result 
# (2) num and den have different signs, and int result is 0, the sign could be omitted in result if we multiply sign with the int result
# (3) the repeating may not begin from the digit just after '.', for example, 1/6=0.1(6)
import unittest
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0: return '0'
        sign, n, d = 1, abs(numerator), abs(denominator)
        if numerator*denominator < 0: sign = -1
        
        _int = ('' if sign ==1 else '-') + str(n // d)
        remain = n % d
        if remain == 0: return _int
        
        f, mem = [], {}
        while remain != 0:
            if remain in mem:
                start = mem[remain]
                return _int+'.'+''.join(map(str, f[:start]))+'('+''.join(map(str, f[start:]))+')'
            mem[remain] = len(f)
            remain *= 10
            f.append(remain//d)
            remain %= d
        return _int+'.'+''.join(map(str, f))

    # bug fixed: the repeating may not begin from the digit just after '.', for example, 1/6=0.1(6)
    def fractionToDecimal2(self, numerator, denominator):
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
        history = {}    # We should use dict to map remain to the index of the div
        while remain > 0:
            if remain in history:
                idx = history[remain]
                return res + ''.join(map(str, div_list[:idx])) + '(' + ''.join(map(str, div_list[idx:])) + ')'
            else:
                history[remain] = len(div_list)
                remain *= 10
                div_list.append(remain//denominator)                
                remain %= denominator

        return res + ''.join(map(str, div_list))

class Test(unittest.TestCase):
    def test_1(self):
        test_cases = [(0, 1), (50, 13), (1, 3), (1, 2), (1, 6), (2, -3), (-1, 2), (1, -3), (0, -2)]
        expected = ['0', '3.(846153)', '0.(3)', '0.5', '0.1(6)', '-0.(6)', '-0.5', '-0.(3)', '0']
        obj = Solution()
        for i, case in enumerate(test_cases):
            self.assertEqual((obj.fractionToDecimal(*case)), expected[i])

    def test_2(self):
        test_cases = [(0, 1), (50, 13), (1, 3), (1, 2), (1, 6), (2, -3), (-1, 2), (1, -3), (0, -2)]
        expected = ['0', '3.(846153)', '0.(3)', '0.5', '0.1(6)', '-0.(6)', '-0.5', '-0.(3)', '0']
        obj = Solution()
        for i, case in enumerate(test_cases):
            self.assertEqual((obj.fractionToDecimal2(*case)), expected[i])

if __name__ == '__main__':
    unittest.main(exit = False)