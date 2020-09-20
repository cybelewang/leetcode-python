"""
1062 Longest Repeating Substring

Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

Example 1:

Input: S = "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: S = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: S = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
Example 4:

Input: S = "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.

Constraints:

The string S consists of only lowercase English letters from 'a' - 'z'.
1 <= S.length <= 1500
"""
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        dp = [[0]*(n+1) for _ in range(n+1)]
        res = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if S[i-1] == S[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])
        return res