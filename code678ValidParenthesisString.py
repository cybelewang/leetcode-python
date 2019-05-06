"""
678 Valid Parenthesis String

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. 
We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""
class Solution:
    # https://leetcode.com/problems/valid-parenthesis-string/discuss/107577/Short-Java-O(n)-time-O(1)-space-one-pass
    # another solution is using two stacks to hold positions of '(' and '*'
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # low: number of unmatched '(' when there are '(' and '*' is treated as ')'
        # high: number of unmatched '(' when '*' is treated as '('
        low, high = 0, 0
        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low = max(0, low-1)
                high -= 1
            else:
                low = max(0, low-1)
                high += 1
            
            if high < 0:
                return False

        return low == 0

    # my own DFS solution, TLE
    def checkValidString2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def dfs(s, i, cnt):
            """
            i: current index in s
            cnt: previous number of unmatched '('
            return True if valid else False
            """
            if cnt < 0: # we have more ')' than '(' in s[:i], and there is no way to repair it, so fail immediately
                return False

            if i == len(s):
                return cnt == 0

            if s[i] == '(':
                return dfs(s, i+1, cnt+1)
            elif s[i] == ')':
                return dfs(s, i+1, cnt-1)
            else:
                return dfs(s, i+1, cnt+1) or dfs(s, i+1, cnt-1) or dfs(s, i+1, cnt)
                
        # main
        if s.startswith(')'):
            return False
        else:
            return dfs(s, 0, 0)

    # stack solution
    # use two stacks: "left" holds the index of '(', and "star" holds the index of ')'
    # two pass, first pass treat '*' as '(', but we try to use existing '(' first, then '*'
    # second pass we try to use '*' as ')' to pair remaining '(', the goal is to eliminate all remaining '('
    def checkValidString3(self, s):
        left, star = [], []
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                star.append(i)
            else:
                # c == ')', consume '(' first, '*' second
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()
        
        # now '*' must be ')' or '', try to pair them
        while left and star:
            if left[-1] < star[-1]:
                left.pop()
                star.pop()
            else:
                break
        
        return len(left) == 0

test_cases = ['', '(', ')', '*', '()', '(*)', '(*()', '((*)', ')*)', '*)*)']
for s in test_cases:
    print(s, end = ' -> ')
    print(Solution().checkValidString3(s))