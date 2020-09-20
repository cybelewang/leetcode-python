"""
1047 Remove All Adjacent Duplicates In String

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
 
Example 1:
Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 
Note:
1 <= S.length <= 20000
S consists only of English lowercase letters.
"""
class Solution:
    # stack solution
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        
        return ''.join(stack)

    # two pointer solution
    def removeDuplicates3(self, S: str) -> str:
        s = list(S)
        i = 0
        for j in range(len(S)):
            s[i] = s[j]
            if i > 0 and s[i-1] == s[j]:
                i -= 2
            i += 1
        return ''.join(s[:i])
        
    # follow-up: remove all adjacent repeating letters, for example "abbba" -> ""
    def removeDuplicates2(self, S: str) -> str:
        stack, repeat = [], False
        for c in S:
            if not stack:
                stack.append(c)
                repeat = False
                continue
            if stack[-1] == c:
                repeat = True
            else:
                if repeat:
                    stack.pop()
                if stack and stack[-1] == c:
                    repeat = True
                else:
                    stack.append(c)
                    repeat = False
        
        if repeat:
            stack.pop()
            
        return ''.join(stack)

