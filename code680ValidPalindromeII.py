"""
680 Valid Palindrome II

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

    # 2nd round solution on 6/29/2020
    def validPalindrome2(self, s):
        def helper(s, i, j, deleted):
            """
            i, j are start and end indices (inclusive)
            deleted (boolean) marked if one character has already been deleted
            """
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    if deleted:
                        return False
                    else:
                        return helper(s, i+1, j, True) or helper(s, i, j-1, True)
            
            return True
        
        return helper(s, 0, len(s)-1, False)

    # O(1) space, using two pointers
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, left, right):
            while left < right and s[left] == s[right]:
                left += 1
                right -= 1
            
            return left >= right
        
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        # case 1: left >= right
        if left >= right:
            return True
        # case 2: left < right and s[left] != s[right]
        else:
            return isPalindrome(s, left+1, right) or isPalindrome(s, left, right-1)

test_cases = ['', 'a', 'ac', 'aa', 'aba', 'caba', 'abbca', 'abc']
obj = Solution()
for s in test_cases:
    print(s, end = ' -> ')
    print(obj.validPalindrome(s))