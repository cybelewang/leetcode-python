"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
"""
from collections import defaultdict
class Solution:
    # my own DFS solution
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def dfs(words, occurrence, used, word, start):
            if start == len(word):
                return True
            
            letter = word[start]
            for i in occurrence[letter]:
                if used[i]:
                    continue
                used[i] = True
                if dfs(words, occurrence, used, word, start + 1):
                    return True
                used[i] = False
            
            return False

        # main
        words.sort(key = lambda word: (-len(word), word))   # longer words are smaller, if two words have the same length, then compare the lexicographically order
        occurrence = defaultdict(set)   # key is the letter, and value is a set contains all the indices of "words" where this letter appears
        for i, word in enumerate(words):
            for letter in set(word):
                occurrence[letter].add(i)
        
        used = [False]*len(words)   # if one character has been used from words[i]

        for word in words:
            if dfs(words, occurrence, used, word, 0):
                return word
        
        return ''

words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(Solution().longestWord(words))