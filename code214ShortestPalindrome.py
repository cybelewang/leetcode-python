"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""
class Solution:
    # reverse s and get t, then use KMP's partial match table algorithm to find the longest prefix == suffix in (s + t)
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        
        ss = s + s[::-1]

        # KMP algorithm to generate the partial match table
        length, M = 0, len(ss)
        i, lps = 1, [0]*M
        while i < M:
            if ss[i] == ss[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length == 0:
                    lps[i] = 0
                    i += 1
                else:
                    length = lps[length - 1]
        
        return s[lps[M-1]:][::-1] + s

    # TLE
    def shortestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        end = 0 # end index of the palindrome string
        for i in range(n//2):
            # check if even-length substring [0 to 2i+1] is palindrome
            for j in range(i, -1, -1):
                if s[j] != s[2*i + 1 - j]:
                    break
            else:
                end = max(end, 2*i + 1)
        
        for i in range((n+1)//2):
            # check if odd-length substring [0 to 2i] is palindrome
            for j in range(i-1, -1, -1):
                if s[j] != s[2*i - j]:
                    break
            else:
                end = max(end, 2*i)
        
        return s[end+1:][::-1] + s

obj = Solution()
test_cases = ['','a','aa','ab','aba', 'aaa','aaab', 'abcd']
for case in test_cases:
    print(case, end=' -> ')
    print(obj.shortestPalindrome(case))