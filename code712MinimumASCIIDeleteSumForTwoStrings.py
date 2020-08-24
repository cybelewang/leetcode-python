"""
712 Minimum ASCII Delete Sum for Two Strings

Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].
"""
# similar problems: 583 Delete Operation for Two Strings
class Solution:
    # 1D DP solution
    def minimumDeleteSum(self, s1, s2):
        M, N = len(s1), len(s2)
        dp = [0]*(N+1)
        for j in range(1, N+1):
            dp[j] = dp[j-1] + ord(s2[j-1])
        
        for i in range(1, M+1):
            pre = dp[0] # dp[i-1][0]
            dp[0] += ord(s1[i-1]) # dp[i][0]
            for j in range(1, N+1):
                temp = dp[j]
                if s1[i-1] == s2[j-1]:
                    dp[j] = min(pre, ord(s1[i-1]) + dp[j], ord(s2[j-1]) + dp[j-1])
                else:
                    dp[j] = min(ord(s1[i-1]) + dp[j], ord(s2[j-1]) + dp[j-1])
                pre = temp
               
        return dp[N]

    # direct 2D DP solution
    def minimumDeleteSum2(self, s1: str, s2: str) -> int:
        M, N, INT_MAX = len(s1), len(s2), 2**31 - 1
        dp = [[INT_MAX]*(N+1) for _ in range(M+1)]
        dp[0][0] = 0
        for i in range(1, M+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, N+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        
        for i in range(1, M+1):
            for j in range(1, N+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1], ord(s1[i-1]) + dp[i-1][j], ord(s2[j-1]) + dp[i][j-1])
                else:
                    dp[i][j] = min(ord(s1[i-1]) + dp[i-1][j], ord(s2[j-1]) + dp[i][j-1])
        
        return dp[M][N]

    # my own solution, similar way to find the longest common subsequence
    def minimumDeleteSum3(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = max(dp[i][j], ord(s1[i-1]) + dp[i-1][j-1])
        
        return sum(map(ord, s1)) + sum(map(ord, s2)) - 2*dp[m][n]

test_cases = [('sea', 'eat'), ('delete', 'leet')]
obj = Solution()
for s1, s2 in test_cases:
    print(obj.minimumDeleteSum(s1, s2))