"""
730 Count Different Palindromic Subsequences

Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo 10^9 + 7.

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

Example 1:
Input: 
S = 'bccb'
Output: 6
Explanation: 
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
Example 2:
Input: 
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
Output: 104860361
Explanation: 
There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
Note:

The length of S will be in the range [1, 1000].
Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
"""
# similar problems: 5 Longest Palindromic Substring; 132 Palindrome Partitioning II; 516 Longest Palindromic Subsequence; 647 Palindromic Substrings
class Solution:
    # my own solution by using problem 5, 132, 647's method, but cannot solve the repeating results issue
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        M, n = 10**9 + 7, len(S)
        dp = [[0]*n for _ in range(n)]  # dp[i][j] is the number of non-empty palindromic subsequences that starting with S[i] and ending with S[j]

        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if S[j] == S[i]:
                    for p in range(i+1, j):
                        for q in range(p, j):                            
                            dp[i][j] = (dp[i][j] + dp[p][q])%M
                    
                    dp[i][j] = (dp[i][j] + 1)%M
        #print(dp)
        return sum(sum(dp, []))%M

print(Solution().countPalindromicSubsequences('bccb'))