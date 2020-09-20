"""
161 One Edit Distance

Given two strings s and t, determine if they are both one edit distance apart.
Note: 
There are 3 possiblities to satisify one edit distance apart:
Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:
Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:
Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
"""
class Solution:
    def isOneEditDistance(self, s, t):
        m, n = len(s), len(t)
        if m < n: return self.isOneEditDistance(t, s)
        if m - n > 1:   return False
        for i in range(n):
            if s[i] != t[i]:
                if m == n: return s[i+1:] == t[i+1:]
                elif m == n + 1: return s[i+1:] == t[i:]

        return m == n + 1

    # https://leetcode.com/problems/one-edit-distance/discuss/50098/My-CLEAR-JAVA-solution-with-explanation
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(t), len(s)
        for i in range(min(m, n)):
            if s[i] != t[i]:
                if m == n:
                    return s[i+1:] == t[i+1:]
                elif m < n:
                    return s[i+1:] == t[i:]
                else:
                    return s[i:] == t[i+1:]
        return abs(m - n) == 1

print(Solution().isOneEditDistance("", ""))