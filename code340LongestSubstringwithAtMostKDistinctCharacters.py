"""
340 Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
"""
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k < 1:
            return 0

        m, res = defaultdict(int), 0
        i = 0
        for j, c in enumerate(s):
            m[c] += 1
            while len(m) > k:
                m[s[i]] -= 1
                if m[s[i]] == 0:
                    m.pop(s[i])
                i += 1
            
            res = max(res, j - i + 1)

        return res

s, k = "eceba", 2
print(Solution().lengthOfLongestSubstringKDistinct(s, k))