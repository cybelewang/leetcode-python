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
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/6493182.html
    # 2-D DP
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

    # two 1-D array DP, pre represents dp[i+1][...], and cur represents dp[i][...]
    def longestPalindromeSubseq2(self, s):
        if not s:
            return 0

        n = len(s)
        pre = [0]*n
        for i in range(n-1, -1, -1):
            cur = [0]*n
            cur[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    cur[j] = pre[j-1] + 2
                else:
                    cur[j] = max(pre[j], cur[j-1])
            pre = cur
        
        return pre[-1]

    # one 1-D array DP, pre represents dp[i+1][j-1] and dp represents dp[i][...]
    def longestPalindromeSubseq3(self, s):
        if not s: return 0
        n = len(s)
        dp = [1]*n
        for i in range(n-1, -1, -1):
            pre = 0 # pre represents dp[i+1][j-1], when j is i+1, dp[i+1][i] is invalid (or empty string) so it must be 0
            dp[i] = 1
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre + 2
                else:
                    dp[j] = max(dp[j], dp[j-1])
                pre = temp
        
        return dp[-1]

obj = Solution()
print(obj.longestPalindromeSubseq3('bbaa'))