"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""
from collections import Counter
from heapq import heappush, heappop
class Solution:
    # my own solution by searching how to get a fixed-size heapq: check length every time when adding a new element
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        def mirror(s):
            """
            mirror 'a' to 'z', 'b' to 'y', 'c' to 'x', ...
            we need this function because we need to treat lower alphabetical word as higher comparison value
            """
            return ''.join(map(lambda x: chr(2*ord('a')+25-ord(x)), s))

        count = Counter(words)
        q = []
        for w in count:
            c, m = count[w], mirror(w)
            if len(q) == k:
                freq, top = heappop(q)
                if (freq, top) < (c, m):
                    heappush(q, (c, m))
                else:
                    heappush(q, (freq, top))
            else:
                heappush(q, (c, m))

        res = []
        for _ in range(k):
            res.append(mirror(heappop(q)[1]))

        return res[::-1]

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(Solution().topKFrequent(words, k))