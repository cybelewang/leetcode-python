"""
151 Reverse Words in a String

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
"""
# similar problems: 189 Rotate Array
# For C programmers, use 189 Rotate Array's method: reverse the whole string first, then reverse each individual word.
# be sure to be familiar with str.split() method: without arguments, using whitespace as separator and remove any empty results
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))

obj = Solution()
test_cases = ['', "the sky is blue", " ", "   ", " I  am big   "]
for case in test_cases:
    print(obj.reverseWords(case))