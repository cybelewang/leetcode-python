"""
97 Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""
class Solution:
    # DP solution with dimension of len(s1) x len(s2)
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n, p = len(s1), len(s2), len(s3)
        if (m + n) != p:
            return False

        dp = [[False for j in range(n + 1)] for i in range(m + 1)]
        dp[0][0] = True

        # Initialize the top row where length of s1 is always 0 but s2 length increases from 1 to s2 length
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s3[j-1] == s2[j-1]

        # Initialize the left column where length of s2 is always 0
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s3[i-1] == s1[i-1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # check if s3's last letter matches either s1's last letter or s2's last letter
                dp[i][j] = (dp[i-1][j] and s3[i+j-1] == s1[i-1]) or \
                (dp[i][j-1] and s3[i+j-1] == s2[j-1])

        return dp[m][n]

    # DP solution with dimension of len(s1) x len(s3), easily cause issue because s2 index may exceed length
    def isInterleave2(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n, p = len(s1), len(s2), len(s3)
        if (m + n) != p:
            return False

        if m > n:
            return self.isInterleave2(s2, s1, s3)

        dp = [[False for j in range(p + 1)] for i in range(m + 1)]
        dp[0][0] = True

        # Initialize the top row where length of s1 is always 0 but s3 length increases from 1 to s2 length
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s3[j-1] == s2[j-1]

        # Initialize the diagnoal where length of s2 is always 0
        for i in range(1, m + 1):
            dp[i][i] = dp[i-1][i-1] and s3[i-1] == s1[i-1]

        for i in range(1, m + 1):   # bug fixed: i should start from 1, not 2, because we only processed dp[1][1] but haven't processed dp[1][2:p+1]
            for j in range(i + 1, i + n + 1):   # bug fixed: j should not range to p + 1 because j -i may be larger than s2 length
                # check if s3's last letter matches either s1's last letter or s2's last letter
                dp[i][j] = (dp[i-1][j-1] and s3[j-1] == s1[i-1]) or \
                (dp[i][j-1] and s3[j-1] == s2[j-i-1])

        return dp[m][p]

# 2nd round solution on 9/20/2018
# recursive solution
class Solution2:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        
        if not s1:
            return s2 == s3
        
        if not s2:
            return s1 == s3
        
        return (s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:])) or (s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:]))

test_cases = [('','',''), ('','a','a'), ('','a','b'), ('a','b','c'), ('a','b','ba'),('a','b','ab'),('aabcc','dbbca', 'aadbbcbcac'),('aabcc','dbbca', 'aadbbbaccc')]
obj = Solution2()
for case in test_cases:
    print(', '.join(case), end = ' => ')
    print(obj.isInterleave(case[0], case[1], case[2]))