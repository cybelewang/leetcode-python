"""
115 Distinct Subsequences

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
        dp = [[0 for j in range(len(s)+1)] for i in range(len(t)+1)]
        
        for j in range(len(s)+1):   # because '' always subsequence of all strings
            dp[0][j] = 1
        
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
            
        return dp[len(t)][len(s)]

test_cases = [('rabbbit', 'rabbit'), ('ABCDE', 'ACE')]

obj = Solution()
for case in test_cases:
    print(obj.numDistinct(case[0], case[1]))

