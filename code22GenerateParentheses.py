"""
22 Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = []
    if n < 1:
        return result
    result.append('(')
    left = [1]

    for i in range(2, 2*n + 1): # i represents the current length
        total = len(result)
        for j in range(total):            
            s = result[j]
            l = left[j] # l in previous length (i-1)
            r = i - 1 - l # bug fixed, i is the current target length after adding '(' or ')', but we are looking for r in previous length, which is i - 1
            if l < n: # can add '('
                result.append(s + '(')
                left.append(l + 1)
            if r < l: # can add ')'
                result.append(s + ')')
                left.append(l)
        result = result[total:]
        left = left[total:] # bug fixed, forgot to resize the list
    return result
        

# Recursion solution
"""
def helper(result, s, l, r, n):
    if (l >= n) and (r >= n):
        result.append(s)
        return
    if l < n:
        helper(result, s + '(', l + 1, r, n)
    if r < l:
        helper(result, s + ')', l, r + 1, n)


def generateParenthesis(n):
    result = []
    if n > 0:
        s = ''
        l, r = 0, 0
        helper(result, s, l, r, n)

    return result
"""

# 2nd revisit on 9/17/2018

res = generateParenthesis(3)
print(res)