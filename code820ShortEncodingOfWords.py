"""
820 Short Encoding of Words

Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].
Note:

1 <= words.length <= 2000.
1 <= words[i].length <= 7.
Each word has only lowercase letters.
"""

class Solution:
    # Trie solution, https://leetcode.com/problems/short-encoding-of-words/solution/
    def minimumLengthEncoding(self, words):
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)

    # accepted solution using set to save all suffix
    def minimumLengthEncoding2(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key = lambda w: -len(w))
        subwords, res = set(), 0
        for word in words:
            if word in subwords:
                continue
            res += len(word) + 1
            for i in range(len(word)):
                subwords.add(word[i:])
        
        return res

    # first trial, TLE
    def minimumLengthEncoding_TLE(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key = lambda w: -len(w))
        res = len(words[0]) + 1
        for i in range(1, len(words)):
            for j in range(i):
                if words[j].endswith(words[i]):
                    break
            else:
                res += len(words[i]) + 1
        
        return res

#words = ["time", "me", "bell"]  # expected 10
words = ["time", "me", "e", "lime"] # expected 10
print(Solution().minimumLengthEncoding(words))