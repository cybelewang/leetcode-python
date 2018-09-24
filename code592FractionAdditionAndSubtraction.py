"""
592 Fraction Addition and Subtraction

Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. 
The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. 
So in this case, 2 should be converted to 2/1.

Example 1:
Input:"-1/2+1/2"
Output: "0/1"
Example 2:
Input:"-1/2+1/2+1/3"
Output: "1/3"
Example 3:
Input:"1/3-1/2"
Output: "-1/6"
Example 4:
Input:"5/3+1/3"
Output: "2/1"
Note:
The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1,10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
"""
# similar problems: 224, 227 Basic Calculator
# see C++ io stream trick http://www.cnblogs.com/grandyang/p/6954197.html
from functools import reduce
class Solution:
    # my own solution, split expression by '/', then unpack numerators and denominators to two lists, then use reduce to get the result
    # use problem 365's Euclidean algorithm to get the greatest common divisor to achieve the irreducible result
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # ask about empty input
        if not expression:
            return '0/1'
            
        parse = expression.split('/')
        n = len(parse)


        nums, denums = [0]*(n-1), [0]*(n-1) # bug fixed: there are only (n-1) pairs, not n pairs
        nums[0] = int(parse[0])
        denums[-1] = int(parse[-1])
        for i in range(1, n-1):
            sub = parse[i]
            index = sub.find('+')
            if index == -1:
                index = sub.find('-')
            denums[i-1] = int(sub[:index])
            nums[i] = int(sub[index:])
        
        num, denum = reduce(self.add, zip(nums, denums))

        return '0/1' if num == 0 else str(num)+'/'+str(denum)

    def gcd(self, x, y):
        """
        get greatest common divisor of x and y
        famous Euclidean algorithm
        """
        return x if y == 0 else self.gcd(y, x % y)

    def add(self, f1, f2):
        """
        f1 = a/b, f2 = c/d
        add a/b + c/d and return the num and denum in irreducible form
        """
        a,b = f1
        c,d = f2
        num = a*d + b*c
        denum = b*d
        factor = self.gcd(num, denum)
        return (num//factor, denum//factor)

expression = "-1/2+1/2+1/3+1/6+1/3"
print(Solution().fractionAddition(expression))