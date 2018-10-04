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