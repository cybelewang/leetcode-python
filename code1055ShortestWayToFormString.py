"""
1055 Shortest Way to Form String

From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.
"""
class Solution:
    # https://leetcode.com/problems/shortest-way-to-form-string/discuss/330938/Accept-is-not-enough-to-get-a-hire.-Interviewee-4-follow-up
    # time O(M+N), space O(M)
    def shortestWay(self, source, target):
        m, n = len(source), len(target)
        # idx[i][x] is the next search start position after finding letter x in source from position i
        # for example, if source = 'abc', then idx[0]['a'] = 1, idx[0]['b'] = 2, idx[0]['c'] = 3, idx[0]['d'] = 0
        # if idx[0][x] = 0, that means the letter x doesn't exist in source
        # if idx[i][x] = m, that means we need to search from the beginning of source, so we  
        idx = [[0]*26 for _ in range(m)]
        pos = ord(source[m-1]) - ord('a')
        idx[m-1][pos] = m
        for i in range(m-2, -1, -1):
            pos = ord(source[i]) - ord('a')
            for k in range(26):
                idx[i][k] = idx[i+1][k]
            idx[i][pos] = i+1
        
        res, i, j = 1, 0, 0
        while j < n:
            pos = ord(target[j]) - ord('a')
            if idx[0][pos] == 0:
                return -1
            # if start position is the end of source, then we need to rewind start to 0 and increment result
            if i == m:
                res += 1
                i = 0
            i = idx[i][pos]
            # if next start position is 0, this means we cannot find target[j] in source[i:]
            # we should rewind the search position to 0 (increment result) and search target[j] again
            if i == 0:
                res += 1
                j -= 1
            j += 1
        
        return res

    # my own DP solution, time O(m*m*n), TLE
    def shortestWay2(self, source, target):
        def isSubsequence(s, t):
            # check if t is subsequence of s
            m, n = len(t), len(s)
            if m == 0: return True
            if m > n: return False
            j = 0
            for i in range(n):
                if j < m and s[i] == t[j]:
                    j += 1
            
            return j == m
        
        m, n = len(source), len(target)
        dp = [2**31 - 1]*(n + 1)
        dp[0] = 0
        for j in range(1, n+1):
            for i in range(max(j-m, 0), j):
                if isSubsequence(source, target[i:j]):
                    dp[j] = min(dp[j], dp[i] + 1)
        
        if dp[-1] == 2**31 - 1:
            return -1
        else:
            return dp[-1]

source, target = "abc", "abcbc"
print(Solution().shortestWay(source, target))