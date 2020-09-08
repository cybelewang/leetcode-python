"""
227 Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
"""
class Solution:
    # OJ best solution, temporarily save previous operator (default is '+') instead of checking previous operator from stack
    # two rounds, first round calculate all operations with '*' and '/', and put the result into a list. In second round just add all the results
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        prev_op = '+'
        s = s + '+'
        for n in s:
            if n.isdigit():
                num = num * 10 + ord(n) - ord('0')
            elif n == ' ':
                continue
            else:
                # we see an operator, so we need to finish parsing the number and start calculation
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack[-1] = stack[-1] * num
                else:
                    # in python -3 / 2 == -2, since when dividing Python uses Floor division.
                    stack[-1] = int(stack[-1] * 1.0 / num)
                num = 0
                prev_op = n
        return sum(stack)

    # generic solution
    def calculate_generic(self, s):
        l1, o1, l2, o2 = 0, 1, 1, 1
        i, n = 0, len(s)
        while i < n:
            if s[i].isdigit():
                j = i + 1
                while j < n and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                l2 = l2 * num if o2 == 1 else l2 // num
                i = j - 1
            elif s[i] in ('+', '-'):
                # level 1 operator
                l1 = l1 + o1 * l2
                o1 = 1 if s[i] == '+' else -1
                o2, l2 = 1, 1
            elif s[i] in ('*', '/'):
                # level 2 operator
                o2 = 1 if s[i] == '*' else -1
            
            i += 1
        
        return l1 + o1 * l2

    def calculate2(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        for (i, c) in enumerate(s):
            if c.isdigit():
                num = num*10 + ord(c) - ord('0')
            if i == len(s) - 1 or c in ('+', '-', '*', '/'):  # when parsing the end character or encounters an operator, we need to finish parsing the number. Fixed a bug, previously used 'elif', which will ignore the last letter processing
                if len(stack) > 0 and (stack[-1] == '*' or stack[-1] == '/'):
                    symbol = stack.pop()
                    param = stack.pop()
                    if symbol == '*':
                        num *= param
                    else:
                        num = param//num                    
                stack.append(num)
                if i < len(s) - 1:
                    stack.append(c)
                num = 0

        res, sign = 0, 1
        for e in stack:
            if e == '+':
                sign = 1
            elif e == '-':
                sign = -1
            else:
                res += sign*e
        
        return res

obj = Solution()
test_cases = ['3 + 2*2', '31 +2*2/3 - 1 ', '3+5 / 2']
for case in test_cases:
    print(case, end = ' = ')
    print(obj.calculate(case))