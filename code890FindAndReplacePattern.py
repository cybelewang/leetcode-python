"""
890 Find and Replace Pattern

You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.

Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
"""
# similar problems: 205 Isomorphic Strings, 290 word pattern
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word, pattern):
            return all(map(lambda w: word.find(w[0]) == pattern.find(w[1]), zip(word, pattern)))  # becareful of lambda, it should take one argument, instead of two
            # for i, a in enumerate(word):
            #     b = pattern[i]
            #     if pattern.index(b) != word.index(a):
            #         return False

            # return True
        
        return [word for word in words if match(word, pattern)]

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        base = list(map(pattern.index, pattern))
        return [word for word in words if list(map(word.index, word)) == base]

words, pattern = ["abc","deq","mee","aqq","dkd","ccc"], "abb"
print(Solution().findAndReplacePattern(words, pattern))