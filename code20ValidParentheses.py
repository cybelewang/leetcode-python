"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Seen this question in a real interview before?
"""

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for c in s:
        if len(stack) == 0:
            stack.append(c)
        else:
            if c == ')' and stack[-1] == '(':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(c)
    
    return len(stack) == 0

test_cases = ["","()", "()[]{}", "][()", "(]", "([)]", "((((())[])){})"]

for test_case in test_cases:
    print(isValid(test_case))