"""
415 Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
# zip takes the shortest, and itertools.zip_longest takes the longest input and optional fillvalue
from itertools import zip_longest
import unittest
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # check '' + '', '' + '1'
        base, carry, digits = ord('0'), 0, []
        for x, y in zip_longest(reversed(num1), reversed(num2), fillvalue='0'):
            add_res = ord(x) + ord(y) - 2*base + carry
            digits.append(chr(add_res%10 + base))
            carry = add_res//10
        
        if carry:
            digits.append(chr(carry + base))

        return ''.join(reversed(digits))

# follow-up: add two strings with dots, like "1.2" + "2.31" = "3.51"
# FB interview question https://www.1point3acres.com/bbs/thread-596207-1-1.html
# we need to split num1 and num2 to integer part and fraction part by '.'
# for integer part, we align right and add from right to left
# for fraction part, we align left and add from right to left
# so we need to make the length equal to avoid alignment, we can do this by padding '0's on integers' left, and '0's on fractions' right
# if the added fraction result longer than input fractions, this means we have 1 need to be added to the integers part
class FractionAdder:
    def addStrings(self, num1, num2):
        # num1 and num2 must have same length
        def add(num1, num2, carry):          
            ans= []
            for d1, d2 in zip(reversed(num1), reversed(num2)):
                su = ord(d1) + ord(d2) - 2*ord('0') + carry
                ans.append(chr(su%10 + ord('0')))
                carry = su//10
            
            if carry:
                ans.append(chr(carry+ord('0')))
            
            return ''.join(reversed(ans))
        
        # get integers and fraction parts
        num1f = ''
        if num1.count('.') > 0:
            num1, num1f = num1.split('.')

        num2f = ''
        if num2.count('.') > 0:
            num2, num2f = num2.split('.')

        # align integers string length by padding '0's on left
        int_max_length = max(len(num1), len(num2), 1)
        num1 = num1.zfill(int_max_length)
        num2 = num2.zfill(int_max_length)
        # align fractions string length by padding '0's on right
        fraction_max_length = max(len(num1f), len(num2f), 1)
        num1f += '0'*(fraction_max_length - len(num1f))
        num2f += '0'*(fraction_max_length - len(num2f))
        # add fraction part
        fraction = add(num1f, num2f, 0)
        carry = 0
        if len(fraction) > fraction_max_length:
            carry = 1
            fraction = fraction[1:]
        fraction = fraction.rstrip('0')
        # add integer part
        integers = add(num1, num2, carry)
        return integers + '.' + fraction if fraction else integers

class AddIntegerTest(unittest.TestCase):
    def test_1(self):
        obj = Solution()
        self.assertEqual(obj.addStrings('123', '4567'), '4690')

class AddFractionTest(unittest.TestCase):
    def test_1(self):
        obj = FractionAdder()
        self.assertEqual(obj.addStrings('123', '4567'), '4690')
        self.assertEqual(obj.addStrings('0.0', '1'), '1')
        self.assertEqual(obj.addStrings('1.', '1'), '2')
        self.assertEqual(obj.addStrings('0.90', '.1'), '1')
        self.assertEqual(obj.addStrings('32.1', '.99'), '33.09')
        self.assertEqual(obj.addStrings('32.111', '.889'), '33')
        self.assertEqual(obj.addStrings('.1', '.2'), '0.3')

unittest.main(exit=False)