"""
1048 Longest String Chain

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
 
Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
"""
from collections import defaultdict
class Solution:
    # sort given words by their length, then use map to save the longest length ending with key, then update the map
    def longestStrChain(self, words):
        words.sort(key = len)
        dp, res = {}, 0
        for w in words:
            dp[w] = max(dp.get(w[:i]+w[i+1:], 0) + 1 for i in range(len(w)))
            res = max(res, dp[w])

        return res
    # my own solution with bugs fixed
    # first group all same size words to a dict with key as the string length, value as a set of words with the same length
    # secondly iterate all sizes, and if current length - previous length = 1, iterate all combinations of previous word s and current word t and see if they can form string chain
    # if s is predecessor of t, assign t's root to s's root, and update result with the length diff + 1 
    def longestStrChain(self, words):
        # helper to validate if s is predecessor of t
        def validate(s, t):
            i = 0
            while i < len(s):
                if s[i] == t[i]:
                    i += 1
                else:
                    break
            return s[i:] == t[i+1:]
        # generate a map to group same size words in a set
        sameSizeWords = defaultdict(set)
        for word in words:
            sameSizeWords[len(word)].add(word)
        # sort the sizes
        sizes = sorted(sameSizeWords.keys())
        if len(sizes) < 2: return 1

        # root[word] is the head of the string chain
        root, res = {}, 0
        for word in sameSizeWords[sizes[0]]:
            root[word] = word
        
        for i in range(1, len(sizes)):
            cur, pre = sizes[i], sizes[i-1]
            if cur - pre == 1:
                for s in sameSizeWords[pre]:
                    for t in sameSizeWords[cur]:
                        if validate(s, t):
                            root[t] = root[s]
                            res = max(res, len(t) - len(root[t]) + 1)
                        else: # bug fixed: forgot to handle the scenario when s is not predecessor of t
                            if t not in root: # bug fixed: t may already exist in root with shorter 
                                root[t] = t
                            
        return res

words = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"] # expect 7
print(Solution().longestStrChain(words))