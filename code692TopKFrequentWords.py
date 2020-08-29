"""
692 Top K Frequent Words

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
from heapq import heapify, heappush, heappop
class Solution:
    # correct solution from https://blog.csdn.net/fuxuemingzhu/article/details/79559691
    # Key idea is that heapify is O(n) time, and heappush, heappop is in O(logn) time
    # So we don't need to maintain a size-k priority queue, but use heapify to get a minHeap (not totally sorted), then use heappop to get first K elements
    # this avoids reverse priority of a string, as in topKFrequent2's mirror function
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)
        q = [(-freq, word) for word, freq in count.items()]
        heapify(q)

        return [heappop(q)[1] for _ in range(k)] 

    # follow-up: find top K frequent words in a large file
    # use Trie to save the counts instead of hashmap (or Counter), then heappushpop the size-k minHeap
    
    # Wrong Solution, test ['a', 'aa', 'aaa']
    # the mistake is the mirror function, which cannot guarantee mirror('a') > mirror('aa')
    # my own solution by searching how to get a fixed-size heapq: check length every time when adding a new element
    # the challenge is how to make 'a' larger than 'aa'
    def topKFrequent2(self, words, k):
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