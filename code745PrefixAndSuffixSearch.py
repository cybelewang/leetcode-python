"""
745 Prefix and Suffix Search

Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). 
It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:
Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1
Note:
words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.
"""
# two solutions
# solution 1: for each word, generate all possible "prefix#suffix" string and put in a map with weight i. (trick of using '#') In function f, we just need to find value of "prefix#suffix". Time O(1), Space O(N*L^2), with N the length of array words, L the length of single word
# solution 2: for each word, get a list of weights that starts with prefix, and get a list of weights that ends with suffix. Then find the biggest overlapping weight. Time O(NL), Space O(N)
class WordFilter:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        pre_index, suf_index = [], []
        for i, word in enumerate(self.words):
            if word.startswith(prefix):
                pre_index.append(i)
            if word.endswith(suffix):
                suf_index.append(i)

        while pre_index and suf_index:
            i, j = pre_index[-1], suf_index[-1]
            if i == j:
                return i
            elif i > j:
                pre_index.pop()
            else:
                suf_index.pop()

        return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

obj = WordFilter(["apple"])
print(obj.f("a", "e")) # returns 0
print(obj.f("b", "")) # returns -1