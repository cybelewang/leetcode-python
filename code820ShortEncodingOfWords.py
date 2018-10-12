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
    def minimumLengthEncoding(self, words):
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

words = ["time", "me", "bell"]  # expected 10
words = ["time", "me", "e", "lime"] # expected 10
print(Solution().minimumLengthEncoding(words))