"""
224 Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.

"""
class Solution:
    # stack solution, when see a '(', push previous result and sign into stack, then start evaluating the expression within '()'.
    # when seeing a ')', pop the previous result and sign out of stack, and continue evaluate the result
    # Be careful if a number is left in stack
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res, num, sign = 0, 0, 1
        for c in s:
            if c.isdigit():
                num = num*10 + ord(c) - ord('0')
            elif c == '+':
                res += sign*num
                num, sign = 0, 1
            elif c == '-':
                res += sign*num
                num, sign = 0, -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif c == ')':
                res += sign*num # value inside this '()'
                num = 0 # reset num                
                res *= stack.pop()
                res += stack.pop()

        res += sign*num

        return res

    # recursive solution, add a number after parsing a number, or after evaluating a (...) part
    def calculate2(self, s):
        """
        :type s: str
        :rtype: int
        """        
        def eval(s, i):
            """
            evaluate expression starting from index i
            return result and next start position
            """
            res, num, sign = 0, 0, 1
            while i < len(s):
                # check if it is a '('
                if s[i] == '(':
                    num, i = eval(s, i+1)
                    res += sign*num
                    num, sign = 0, 1    # bug fixed: num is like a number, must reset num and sign
                    continue

                if s[i] == ')':
                    return (res, i+1)

                # check if it is a sign
                if s[i] == '-':
                    sign *= -1
                    i += 1
                    continue

                # check if it is a digit
                j = i
                while j < len(s) and s[j].isdigit():    # parse the number
                    num = num*10 + ord(s[j]) - ord('0')
                    j += 1

                if j > i:   # has a number, must add it to result and reset num and sign
                    res += sign*num
                    num, sign = 0, 1
                    i = j
                    continue
                
                # anything else like ' ', '+', just ignore it
                i += 1
            
            return (res, i)
        
        res, end = eval(s, 0)

        return res

test_case = '100-(-(2-34)+6 -(9))'
obj = Solution()
print(obj.calculate(test_case))
print(obj.calculate2(test_case))
