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
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2:
            return s
        i = j = 0
        maxLen = 1
        isPalindrome = [[True for x in range(l)] for y in range(l)]
        for x in range(l-2, -1, -1):
            for y in range(x+1, l):
                isPalindrome[x][y] = isPalindrome[x+1][y-1] and (s[x] == s[y])
                if isPalindrome[x][y]:
                    if (y - x + 1) > maxLen:
                        maxLen = y - x + 1
                        i, j = x, y
        
        return s[i: j+1]

    # Manacher Algorithm, https://www.cnblogs.com/grandyang/p/4475985.html
    # 6/24/2019
    def longestPalindrome2(self, s):
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