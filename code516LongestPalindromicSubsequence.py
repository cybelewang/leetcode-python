"""
516 Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""
# TODO: try 1-D DP
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/6493182.html
    # DP
    # For palindrome, use sequence recurrsion relation, but i should scan from end to beginning, and j should be from i to end
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)        
        dp = [[0]*n for _ in range(n)]  # dp[i][j] is the length of longest palindromic subsequence of s[i:j+1], so only when i <= j dp[i][j] is valid, for invalid i > j, dp[i][j] is 0
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]

obj = Solution()
print(obj.longestPalindromeSubseq('bbaa'))