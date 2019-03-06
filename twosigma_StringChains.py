"""
String Chains

Given an array of words, choose a word from it and in each step, remove a single letter from the chosen word if and only if doing so yields another word that is already in the words array. 
Keep doing this until the resulting string is not in words array. Find the maximum number of strings in a chain of successive character removals.

Example:
words = ["a", "b", "ba", "bca", "bda", "bdca"]
result = 4
Explanation:
There are four chains with length 4:
"bdca"->"bda"->"ba"->"a"
"bdca"->"bda"->"ba"->"b"
"bdca"->"bca"->"ba"->"a"
"bdca"->"bca"->"ba"->"b"
Other chains have smaller length.
"""
class Solution:
    def longestChain(self, words):
        """
        :type words: list[str]
        :rtype: int
        """
        def dfs(word, cache):
            """
            word: the current starting word
            cache: the dict
            returns the longest chain length starting from words[i]
            """
            if cache[word] > 0:
                return cache[word]
            
            maxLen = 1
            for i in range(len(word)):
                s = word[:i] + word[i+1:]
                if s in cache:
                    maxLen = max(maxLen, dfs(s, cache) + 1)
            
            cache[word] = maxLen
            return maxLen

        # main
        words.sort(key = lambda word: -len(word))   # reversely sort the words array by length
        cache = {word:0 for word in words}  # default value is 0, which means the word has not been searched

        res = 0
        for word in words:
            res = max(res, dfs(word, cache))
        
        return res
        
test_case = ["a", "b", "ba", "bca", "bda", "bdca"]
print(Solution().longestChain(test_case))