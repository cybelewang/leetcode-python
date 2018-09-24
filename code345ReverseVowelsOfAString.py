"""
345 Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""
from collections import deque
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a','e','i','o','u', 'A','E','I','O','U'])
        chars = list(s)
        vowelIndex = deque()
        for i,c in enumerate(chars):
            if c in vowels:
                vowelIndex.append(i)

        while len(vowelIndex) > 1:
            l = vowelIndex.popleft()
            r = vowelIndex.pop()
            chars[l], chars[r] = chars[r], chars[l]
        
        return ''.join(chars)

test_case = "nnyyab"
obj = Solution()
print(obj.reverseVowels(test_case))