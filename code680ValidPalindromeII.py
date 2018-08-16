"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""
class Solution:
    # my own solution
    # need to consider both cases: remove s[i] and remove s[j]
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def checkPalindrome(s, i, j):
            # check palindrome at both ends
            # return the first position pair where s[i] != s[j]
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    break

            return (i, j)

        # main    
        n = len(s)

        # check if s is a palindrome
        i, j = checkPalindrome(s, 0, n-1)
        if i >= j:
            return True

        # now try to remove s[i]
        if s[i+1] == s[j]:
            p, q = checkPalindrome(s, i+1, j)
            if p >= q:
                return True

        # now try to remove s[j]
        if s[i] == s[j-1]:
            p, q = checkPalindrome(s, i, j-1)
            if p >= q:
                return True

        return False

test_cases = ['', 'a', 'ac', 'aa', 'aba', 'caba', 'abbca', 'abc']
obj = Solution()
for s in test_cases:
    print(s, end = ' -> ')
    print(obj.validPalindrome(s))