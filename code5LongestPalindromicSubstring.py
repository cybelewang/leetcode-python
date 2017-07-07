# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

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
                