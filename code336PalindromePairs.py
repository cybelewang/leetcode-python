"""
336 Palindrome Pairs

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""
class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        if len(words) < 2:
            return res
        
        word_index = {word:i for i, word in enumerate(words)}
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                str1, str2 = word[:j], word[j:]
                if self.isPalindrome(str1):
                    rev_str2 = str2[::-1]
                    if rev_str2 in word_index and word_index[rev_str2] != i:
                        res.append([word_index[rev_str2], i])
                
                if len(str2) != 0 and self.isPalindrome(str2):  # pitfall here: check str2 != '' to avoid duplicates
                    rev_str1 = str1[::-1]
                    if rev_str1 in word_index and word_index[rev_str1] != i:
                        res.append([i, word_index[rev_str1]])

        return res

    def isPalindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    # naive solution, TLE
    def palindromePairs2(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n = len(words)
        res = []
        for i in range(n):
            for j in range(n):
                if i != j and self.isPalindrome(words[i] + words[j]):
                    res.append([i, j])

        return res

words = ["abcd", "dcba", "lls", "s", "sssll"]
obj = Solution()
print(obj.palindromePairs(words))