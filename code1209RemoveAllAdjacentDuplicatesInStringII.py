"""
1209 Remove All Adjacent Duplicates in String II

Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

Constraints:
1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lower case English letters.
"""
import unittest
from itertools import groupby
from functools import lru_cache
class Solution:
    # my own two stack solution O(N) time, O(N) space
    def removeDuplicates(self, s, k):
        letters = []
        count = []
        for c in s:
            if not letters or letters[-1] != c:
                letters.append(c)
                count.append(1)
            else: # letters[-1] == c
                count[-1] += 1
                if count[-1] == k:
                    letters.pop()
                    count.pop()
        res = ''
        for c, k in zip(letters, count):
            res += c*k
        return res

    def removeDuplicates(self, s: str, k: int) -> str:
        a, n = list(s), len(s)
        i, count = 0, [0]*n
        for j in range(len(s)):
            a[i] = a[j]
            if i > 0 and a[j] == a[i-1]:
                count[i] = count[i-1] + 1
                if count[i] == k:
                    i -= k
            else:
                count[i] = 1
            i += 1
        return ''.join(a[:i])

    # BLP follow-up: remove all >= k continuous repeating letters
    # instead of checking cnt[-1] == 0, we just pop two stacks if the count >= k, but this won't pass "aabbbaaabba", which expects ""
    def removeDuplicates2(self, s, k):
        letters, cnt = [], []
        i = 0
        while i < len(s):
            c = s[i]
            if not letters:
                letters.append(c)
                cnt.append(1)
                i += 1
                continue
            if c == letters[-1]:
                cnt[-1] += 1
                i += 1
                continue
            if cnt[-1] >= k:
                # note there is no i += 1 here
                letters.pop()
                cnt.pop()
            else:
                letters.append(c)
                cnt.append(1)
                i += 1
        # don't forget to process the last unique letters
        if cnt and cnt[-1] >= k:
            letters.pop()
            cnt.pop()
                
        res = ''
        for letter, count in zip(letters, cnt):
            res += letter*count
        
        return res
    
    # BLP follow-up
    # two direction that fix the bug for cause "aabbbaaabba", but still has bug on the very long input case
    def removeDuplicates3(self, s, k):
        s1 = self.removeDuplicates2(s, k)
        s2 = self.removeDuplicates2(s[::-1], k)
        if len(s1) < len(s2):
            return s1
        else:
            return s2[::-1]

    # BLP follow-up
    # use backtracking to iterate all combinations of 3 adjacent chars, checking every time if the result is an improvement
    @lru_cache()
    def bestCandyCrush(self, s):
        l, segs = 0, []
        for c, seq in groupby(s):
            k = len(list(seq))
            if k >= 3:
                segs.append((l, l+k))
            l += k
        return min([self.bestCandyCrush(s[:l] + s[r:]) for l, r in segs], key = len, default = s)

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().removeDuplicates3("aabbbaaabba", 3), "")
        self.assertEqual(Solution().bestCandyCrush("aaabbbacd"), "cd")
        #self.assertEqual(Solution().bestCandyCrush("baaabbbabbccccdbaaabbbabbdccccdaaabbbbaaabbbabbccccdbaaadbbbabbccccdaaabbb"), "dabbd")

unittest.main(exit = False)