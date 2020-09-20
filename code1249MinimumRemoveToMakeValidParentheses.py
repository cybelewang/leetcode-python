"""
1249 Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters. 
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 
Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 
Constraints:
1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""
class Solution:
    # use stack to keep the invalid '(' or ')' positions and then remove them
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
            
        a = list(s)
        for i in stack:
            a[i] = ''
        
        return ''.join(a)

    # non-stack solution
    # approach 3 in https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/solution/
    def minRemoveToMakeValid(self, s: str) -> str:
        # 1st pass to remove invalid ')'
        ans, open_parenthesis, balance = [], 0, 0
        for c in s:
            if c == '(':
                open_parenthesis += 1
                balance += 1
            elif c == ')':
                if balance == 0:
                    continue
                balance -= 1
            ans.append(c)
        
        # 2nd pass to remove most right '('
        open_to_keep = open_parenthesis - balance
        for i, c in enumerate(ans):
            if c == '(':
                if open_to_keep == 0:
                    ans[i] = ''
                    continue
                open_to_keep -= 1
        
        return ''.join(ans)

    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        cnt = 0
        for i, c in enumerate(s):
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt > 0:
                    cnt -= 1
                else:
                    s[i] = ''
        #print(s)
        cnt = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                cnt += 1
            elif s[i] == '(':
                if cnt > 0:
                    cnt -= 1
                else:
                    s[i] = ''
        #print(s)
        return ''.join(s)
                