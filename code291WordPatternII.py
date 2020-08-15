"""
291 Word Pattern II

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Example 1:

Input: pattern = "abab", str = "redblueredblue"
Output: true
Example 2:

Input: pattern = "aaaa", str = "asdasdasdasd"
Output: true
Example 3:

Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false
 
Constraints:
You may assume both pattern and str contains only lowercase letters.
"""
import unittest
class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        def helper(p, i, s, j, m1, m2):
            # i: p's start index
            # j: s's start index
            # return True if we find 
            if i >= len(p) or j >= len(s):
                return i == len(p) and j == len(s)

            if p[i] in m1:
                if not s[j:].startswith(m1[p[i]]):
                    return False
                else:
                    return helper(p, i+1, s, j+len(m1[p[i]]), m1, m2)
            else:
                for k in range(j+1, len(s)+1):
                    t = s[j:k]
                    # if t exists in m2, that means another letter in p maps to t, and we can't use t
                    if t not in m2:
                        m1[p[i]] = t
                        m2[t] = p[i]
                        if helper(p, i+1, s, k, m1, m2):
                            return True
                        m1.pop(p[i])
                        m2.pop(t)
                return False
        return helper(pattern, 0, str, 0, {}, {})

class Test(unittest.TestCase):
    def test_1(self):
        obj = Solution()
        self.assertFalse(obj.wordPatternMatch("ab", "aa"))
        self.assertTrue(obj.wordPatternMatch("aaaa", "asdasdasdasd"))

unittest.main(exit = False)