import collections
"""
150 Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
# be careful of -12//8 = -2
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = collections.deque()
        for s in tokens:
            if s == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif s == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif s == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            elif s == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                if num1 * num2 >= 0:
                    stack.append(num2 // num1)
                else:
                    stack.append(-1*(abs(num2)//abs(num1)))
            else:
                stack.append(int(s))
        
        return stack[0]

obj = Solution()
test_case = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(obj.evalRPN(test_case))