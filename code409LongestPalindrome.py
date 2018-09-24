"""
409 Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
from collections import defaultdict
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        res, hasOdd = 0, False
        for c in count:
            hasOdd = hasOdd or (count[c] & 1)
            res += count[c]//2

        return 2*res + hasOdd

test_cases = ['', 'a', 'aa', "abccccdde"]
obj = Solution()
for s in test_cases:
    print(obj.longestPalindrome(s))