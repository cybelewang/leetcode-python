"""

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
"""
class Solution:
    # my own solution, use DP to find out the length of the longest common subsequence between word1 and word2, this longest common subsequence will be the final string that make word1 == word2
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]    # dp[i][j] is the length of longest common subsequence between word1[0:i] and word2[0:j], here i, j are the length of wrod1 and word2

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return m + n - 2*dp[m][n]

test_cases = [('', ''), ('sea', 'eat'), ('eda','dea'), ('abc', 'cba'), ('abc', 'abc')]
obj = Solution()
for word1, word2 in test_cases:
    print(word1, word2, sep=', ', end = ' -> ')
    print(obj.minDistance(word1, word2))