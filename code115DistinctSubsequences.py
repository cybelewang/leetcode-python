"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""
class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t):
            return 0

        if t == '':
            return 1

        base = list(s)  # base list of all characters of s
        build = []

        res = self._dfs(base, build, si, t, ti):

        return res

    def _dfs(self, base, build, si, t, ti):
        if len(t) - ti > len(base) - si:
            return 0
        
        if t == ''.join(build):
            return 1

        for j in range(ti, len(t)):
            

