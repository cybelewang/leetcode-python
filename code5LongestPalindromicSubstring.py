"""
5 Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""
class Solution(object):
    # Expand from center, O(N^2) time, O(1) space
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left, right):
            # return longest palindromic length
            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1 # bug fixed: not (right - left + 1)
        
        start, end = 0, 0
        for i in range(len(s)):
            odd = expand(s, i, i)
            even = expand(s, i, i+1)
            length = max(odd, even)
            if end - start < length:
                start = i - (length-1)//2
                end = i + length//2 + 1
            
        return s[start:end]

    # DP method, O(N^2) time, O(N^2) space
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        if N < 2:
            return s
        i = j = 0
        maxLen = 1
        P = [[True]*N for _ in range(N)]
        for i in range(N-2, -1, -1):
            for j in range(i+1, N):
                P[i][j] = P[i+1][j-1] and (s[i] == s[j])
                if P[i][j]:
                    if (j - i + 1) > maxLen:
                        maxLen = j - i + 1
                        start, end = i, j+1
        
        return s[start:end]

    # Manacher Algorithm, https://www.cnblogs.com/grandyang/p/4475985.html
    # 6/24/2019
    def longestPalindrome3(self, s):
        # insert '$' and '#' to change from "abc" to "$#a#b#c"
        t = '$#' + '#'.join(s) + '#'
        N = len(t)

        # process t
        p = [0]*N
        mx, id, resLen, resCenter = 0, 0, 0, 0
        for i in range(1, N):
            p[i] = min(p[2*id - i], mx - i) if mx > i else 1
            while t[i+p[i]] == t[i-p[i]]:
                p[i] += 1
            
            if mx < i + p[i]:
                mx = i + p[i]
                id = i
            
            if resLen < p[i]:
                resLen = p[i]
                resCenter = i
        
        start = (resCenter - resLen)//2
        return s[start:start+resLen-1]

s = "122122"
print(Solution().longestPalindrome2(s))