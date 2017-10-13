"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) < 1:
            return 0
        
        end = len(s) - 1
        while end > -1 and s[end] == ' ':
            end -= 1
 
        start = end
        while start > -1 and s[start] != ' ':
            start -= 1
        
        return end - start

obj = Solution()
test_cases = ['', ' ', '   ', '  a   ', 'abc', 'Hellow World', 'a b c d']
for case in test_cases:
    print(case, end = ' -> ')
    print(obj.lengthOfLastWord(case))