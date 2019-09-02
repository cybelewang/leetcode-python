"""
358 Rearrange String k Distance Apart

Given a non-empty string str and an integer k, rearrange the string such that the same characters are at least distance k from each other.
All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:
str = "aabbcc", k = 3
Result: "abcabc"
The same letters are at least distance 3 from each other.

Example 2:
str = "aaabc", k = 3 
Answer: ""
It is not possible to rearrange the string.

Example 3:
str = "aaadbbcc", k = 2
Answer: "abacabcd"
Another possible answer is: "abcabcda"
The same letters are at least distance 2 from each other.
"""
from collections import Counter
from heapq import heappush, heappop
class Solution:
    def rearrangeString(self, s, k):
        """
        rtype: str
        """
        if k == 0:
            return s
        
        m, n = Counter(s), len(s)
        heap = []
        for char in m:
            heappush(heap, [-m[char], char])
        
        res = ''
        while heap:
            v, cnt = [], min(k, n)
            for i in range(cnt):
                if not heap:
                    return ""
                t = heappop(heap)
                res += t[1]
                t[0] += 1
                if t[0] < 0:
                    v.append(t)
                n -= 1
            for a in v:
                heappush(heap, a)

        return res

s, k = "aabbcc", 3        
print(Solution().rearrangeString(s, k))