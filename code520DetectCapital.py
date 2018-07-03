"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

"""
class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word in (word.upper(), word.lower(), word[:1].upper()+word[1:].lower())  # don't use word[0], instead using word[:1] to avoide index out of range exception

test_cases = ['a', 'A', 'USA', 'leetcode', 'Google', 'FlaG']
obj = Solution()
for word in test_cases:
    print(word, end=' -> ')
    print(obj.detectCapitalUse(word))