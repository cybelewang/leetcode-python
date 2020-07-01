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
        
        index = {word:i for i, word in enumerate(words)}
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left, right = word[:j], word[j:]
                if left == left[::-1]:
                    rev_right = right[::-1]
                    if rev_right in index and index[rev_right] != i:
                        res.append([index[rev_right], i])
                
                if right != '' and right == right[::-1]:  # pitfall here: check right != '' to avoid duplicates
                    rev_left = left[::-1]
                    if rev_left in index and index[rev_left] != i:
                        res.append([i, index[rev_left]])

        return res

    def isPalindrome(self, s):
        return s == s[::-1]

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