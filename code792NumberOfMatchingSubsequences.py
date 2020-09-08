"""
792 Number of Matching Subsequences

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
"""
from collections import defaultdict
from bisect import bisect_left
class Solution:
    # time O(N*w + S), space O(w)
    # w is the average length of all words in words list
    # N is length of words list
    # S is the length of S
    # Like the sweep line method, we put all iterators of words in a heads list based on their start letter
    # if two words start with letter 'a', then their iterators will be put into the same list of heads['a']
    # Then iterating each letter of S, for each letter, we will advance the iterators in heads[letter]
    # and put the iterators into other heads list based on the iterator's value (letter)
    # If iterator reaches end of the word, that means the word is a subsequence of S and we add ans by 1.
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        # heads[x] contains all iterators of words starting with letter x
        heads = [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            pos = ord(next(it)) - ord('a')
            heads[pos].append(it)
        
        ans = 0
        for c in S:
            pos = ord(c) - ord('a')
            # take the old bucket which contains all word iterators having the letter c
            old_bucket = heads[pos]
            # reset the bucket for new iterators to be put in
            heads[pos] = []
            # process all iterators in old bucket
            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    # put iterator into corresponding bucket based on new letter that iterator gives
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1
        
        return ans

    # time O(N*w*log(S)), space O(S)
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        index = defaultdict(list)
        for i, c in enumerate(S):
            index[c].append(i)

        count = 0
        for w in words:
            limit = 0
            for c in w:
                idx = bisect_left(index[c], limit)
                if idx == len(index[c]):
                    break
                else:
                    limit = index[c][idx] + 1
            else:
                count += 1
        
        return count

S = "abcd"
words = ["a", "bb", "acd", "ace"]
print(Solution().numMatchingSubseq(S, words))