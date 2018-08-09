"""
There is a strange printer with the following two special requirements:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.
Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.

Example 1:
Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:
Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
Hint: Length of the given string will not exceed 100.
"""
# similar problems: 546 Remove Boxes, Burst Balloons, Zuma Game
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/8319913.html
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0]*n for _ in range(n)]  # dp[i][j] is the result for substring s[i:j+1]

        for i in range(n-1, -1, -1):
            dp[i][i] = 1    # 1 for a single-character string
            for j in range(i+1, n):
                dp[i][j] = 1 + dp[i+1][j]   # when appending s[i] to the left of s[i+1:j+1], the worst case is that s[i] is different so one more print
                # k scans from i + 1 to j
                for k in range(i+1, j+1):
                    if s[k] == s[i]:
                        dp[i][j] = min(dp[i][j], dp[i+1][k-1] + dp[k][j])

        return 0 if n == 0 else dp[0][n-1]

test_cases = ['', 'a', 'aba', 'abab', 'abba', 'abcb']
obj = Solution()
for s in test_cases:
    print(s, end = ' -> ')
    print(obj.strangePrinter(s))