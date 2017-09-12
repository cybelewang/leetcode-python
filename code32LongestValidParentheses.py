"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""
# better solution, 59 ms
def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    maxLen = 0
    stack = [-1]
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                maxLen = max(maxLen, i - stack[-1])
    return maxLen


# my own solution, 92 ms
def longestValidParentheses2(s):
    """
    :type s: str
    :rtype: int
    """
    remain = []
    index = []

    for (i, c) in enumerate(s):
        if c == ')' and len(remain) > 0 and remain[-1] == '(':
            remain.pop()
            index.pop()
        else:
            remain.append(c)
            index. append(i)

    length = 0
    start = -1
    for end in index:
        length = max(end - start - 1, length)
        start = end
    
    length = max(len(s) - start - 1, length)

    return length

test_cases = ["", "(", ")", "()", "(()", ")()())", "()()))((", "())()()()" ]
for s in test_cases:
    print(s, end='')
    print(' -> ', end='')
    print(longestValidParentheses(s))