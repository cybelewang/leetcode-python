"""
318 Maximum Product of Word Lengths

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""
class Solution:
    # OJ best solution, use mask to save bits corresponding to 'a'-'z'
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - ord('a')))
            d[mask] = max(d.get(mask, 0), len(w))   # note the good use of dict.get(key, [default])
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0]) # note the good use of "or": if the first list is empty it will return second list, which is [0]

    # my O(n^2) solution, use a map char_pos to store letter and its corresponding string's positions
    # For each string's character, check if this character shows up in previous strings, if yes, put previous strings' positions into shares set
    # Iterate all previous positions and if it is not in shares, take max
    def maxProduct2(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        char_pos, shares = {}, set()
        res = 0
        for i, word in enumerate(words):
            shares.clear()
            for c in word:
                if c in char_pos:
                    shares |= char_pos[c]   # union operation of sets
                    char_pos[c].add(i)
                else:
                    record = set()
                    record.add(i)
                    char_pos[c] = record
            
            for j in range(0, i):
                if j not in shares:
                    res = max(res, len(word)*len(words[j]))
        
        return res

test_case = []
obj = Solution()
print(obj.maxProduct(test_case))