"""
459 Repeated Substring Pattern


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
# KMP solution
# https://www.geeksforgeeks.org/find-given-string-can-represented-substring-iterating-substring-n-times/
# http://www.cnblogs.com/grandyang/p/6087347.html
class Solution(object):
    # https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/Easy-python-solution-with-explaination
    # First char of input string is first char of repeated substring
    # Last char of input string is last char of repeated substring
    # Let S1 = S + S (where S is input string)
    # Remove 1 and last char of S1. Let this be S2
    # If S exists in S2 then return true else false
    # Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
            
        ss = (s + s)[1:-1]
        return ss.find(s) != -1

    # my own solution, wrong solution for test input "abacababacab"
    # initially set substring to be s[0], and set the scan index j on 0 for substring
    # iterate all characters in s, in position i: if s[i] == sub[j], then we advance both i and j
    # if s[i] != sub[j], we reset sub to s[:i] and j to 0, advance i
    # eventually we need to check if len(sub) < len(s) and j points to the end of sub
    def repeatedSubstringPattern2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # check this corner case
        if not s:
            return False

        sub, j = s[0], 0
        for i, c in enumerate(s):
            if c == sub[j%len(sub)]:# we use mod to make j loop from 0 to len(sub) - 1
                j += 1
            else:
                sub = s[:i+1]
                j = 0

        return len(sub) < len(s) and j%len(sub) == 0 # pitfall: should not use j == len(sub)

    # wrong solution, see test case "abaababaab"
    def repeatedSubstringPattern3(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        count = [s.count(chr(c)) for c in range(ord('a'), ord('z')+1)]
        base = min(filter(lambda x: x > 0, count))
        if list(filter(lambda x: x%base != 0, count)):
            return False
        
        length = len(s)//base
        if length == len(s):
            return False

        print(length)
        i, sub = length, s[:length]
        while i + length <= len(s):
            if s[i: i+length] != sub:
                return False
            i += length
        return i == len(s)

s = "abaababaab"
#s = "abacababacab"
obj = Solution()
print(obj.repeatedSubstringPattern(s))