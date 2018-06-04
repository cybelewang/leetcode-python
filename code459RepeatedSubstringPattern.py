"""

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. 
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""
class Solution(object):
    # my own solution
    # initially set substring to be s[0], and set the scan index j on 0 for substring
    # iterate all characters in s, in position i: if s[i] == sub[j], then we advance both i and j
    # if s[i] != sub[j], we reset sub to s[:i] and j to 0, advance i
    # eventually we need to check if len(sub) < len(s) and j points to the end of sub
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # check this corner case
        if not s:
            return True

        sub, j = s[0], 0
        for i, c in enumerate(s):
            if c == sub[j%len(sub)]:# we use mod to make j loop from 0 to len(sub) - 1
                j += 1
            else:
                sub = s[:i+1]
                j = 0

        return len(sub) < len(s) and j%len(sub) == 0 # pitfall: should not use j == len(sub)

s = 'abcabcabcabc'
obj = Solution()
print(obj.repeatedSubstringPattern(s))