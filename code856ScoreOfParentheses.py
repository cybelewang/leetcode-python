"""
856 Score of Parentheses

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
 

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
"""
class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0.5
        
        start, count, res = 0, 0, 0
        for i, c in enumerate(S):
            if c == '(':
                count += 1
            else:
                count -= 1
            
            if count == 0:
                res += 2*self.scoreOfParentheses(S[start+1:i])
                start = i + 1
        
        return int(res)

S = "()()"
print(Solution().scoreOfParentheses(S))