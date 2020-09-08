"""
772 Basic Calculator III

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
 
Note: Do not use the eval built-in library function.
"""
class Solution:
    # Iterative solution, time O(N), space O(N)
    # https://leetcode.com/problems/basic-calculator-iii/discuss/113592/Development-of-a-generic-solution-for-the-series-of-the-calculator-problems
    def calculate(self, s) -> int:
        # level 1 partial result, operator, level 2 partial result, operator
        l1, o1, l2, o2 = 0, 1, 1, 1
        stack, i, n = [], 0, len(s)
        while i < n:
            if s[i].isdigit():
                # number, level 2 evaluation
                j = i + 1
                while j < n and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                l2 = l2 * num if o2 == 1 else l2 // num
                i = j - 1
            elif s[i] in ('+', '-'):
                # level 1 operator, level 1 evaluation
                l1 = l1 + o1 * l2
                o1 = 1 if s[i] == '+' else -1
                # reset level 2 variables
                l2, o2 = 1, 1
            elif s[i] in ('*', '/'):
                # level 2 operator, just update level 2 operator
                o2 = 1 if s[i] == '*' else -1
            elif s[i] == '(':
                # opening parenthesis, push all variables to stack
                stack.append((l1, o1, l2, o2))
                # reset variables
                l1, o1, l2, o2 = 0, 1, 1, 1
            elif s[i] == ')':
                # closing parenthesis, first level 1 evaluation of subexpression inside parenthesis
                num = l1 + o1*l2
                # restore outside variables
                l1, o1, l2, o2 = stack.pop()
                # treat "(...)" as a number, do level 2 evaluation
                l2 = l2 * num if o2 == 1 else l2 // num              
                
            i += 1
        # end of expression, do level 1 evaluation
        return l1 + o1 * l2
    # use 227 Basic Calculator II's method and deal with parenthesis with recursion
    # time O(N^2) because recursion also parses subexpression, space O(N)
    def calculate2(self, s) -> int:
        s += '+'
        n, i = len(s), 0
        a, last_op = [], '+'
        num = 0
        while i < n:
            if s[i].isdigit():
                num = num*10 + ord(s[i]) - ord('0')
            elif s[i] in ('+', '-', '*', '/'):
                if last_op == '+':
                    a.append(num)
                elif last_op == '-':
                    a.append(-num)
                elif last_op == '*':
                    a[-1] *= num
                elif last_op == '/':
                    sign = 1 if a[-1] > 0 else -1
                    a[-1] = sign*(abs(a[-1])//num)
                last_op, num = s[i], 0
            elif s[i] == '(':
                balance, j = 1, i+1
                while j < n:
                    if s[j] == '(':
                        balance += 1
                    elif s[j] == ')':
                        balance -= 1
                        if balance == 0: break
                    j += 1
                num = self.calculate(s[i+1:j])
                i = j
            i += 1
        #print(a)
        return sum(a)