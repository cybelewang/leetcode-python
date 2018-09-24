"""
647 Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
"""
# similar problems: 5 Longest Palindrome Substring; 132 Palindrome Partitioning II
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[False]*n for _ in range(n)]  # dp[i][j] indicates if substring s[i:j+1] is palindromic

        res = 0
        for i in range(n-1, -1, -1):
            dp[i][i] = True
            res += 1    # bug fixed: forgot to update result here
            for j in range(i+1, n):
                dp[i][j] = (s[i]==s[j]) and ((i+1>j-1) or dp[i+1][j-1]) # bug fixed: when i+1>j-1, we searched to the lower-left portion of DP matrix, which has no meaning
                if dp[i][j]:
                    res += 1
        
        return res

s = 'aaa'
print(Solution().countSubstrings(s))