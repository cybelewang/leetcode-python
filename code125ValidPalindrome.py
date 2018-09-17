"""
125 Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            left = s[i]
            right = s[j]
            if not left.isalnum():
                i += 1
            elif not right.isalnum():
                j -= 1
            else:
                if left.lower() != right.lower():
                    return False
                else:
                    i += 1
                    j -= 1
        
        return True

# 2nd round visited

obj = Solution()
test_cases = ['', 'a', ':', "A man, a plan, a canal: Panama", 'race a car']
for case in test_cases:
    print(obj.isPalindrome(case))