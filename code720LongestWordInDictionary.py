"""
720 Longest Word in Dictionary

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
# similar problems: 524 Longest Word in Dictionary through Deleting; 676 Implement Magic Dictionary
# misunderstood the problem: there must be incrementing substrings in words
from collections import defaultdict
class Solution:
    # sort words in aplhabet order, then incremently put word into set if word[:-1] is already in set
    def longestWord_OJBest(self, words):
        words.sort()
        words_set, longest_word = set(['']), ''
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word

    # correct solution after correctly understanding the requirement
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort(key = lambda word: (-len(word), word))
        unique = set(words)
        for word in words:
            for i in range(1, len(word)+1):
                if word[:i] not in unique:
                    break
            else:
                return word
        
        return ''

    # my own DFS solution, misunderstood the requirement: thought need to find a character each time from the rest of strings in words
    def longestWord_WRONG(self, words):
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
        #print(words)
        occurrence = defaultdict(set)   # key is the letter, and value is a set contains all the indices of "words" where this letter appears
        for i, word in enumerate(words):
            for letter in set(word):
                occurrence[letter].add(i)
        
        used = [False]*len(words)   # if one character has been used from words[i]

        for word in words:
            if dfs(words, occurrence, used, word, 0):
                return word
        
        return ''

#words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
words = ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]    # expected: 'yodn'
print(Solution().longestWord(words))