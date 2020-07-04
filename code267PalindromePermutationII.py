"""
267. Palindrome Permutation II

Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.
Example 1:
Input: "aabb"
Output: ["abba", "baab"]
Example 2:
Input: "abc"
Output: []
"""
import unittest
import itertools
from collections import Counter
class Solution:
    # 1st round solution on 6/30/2020 
    # create the first half of palindrome, then concatenate with middle letter ('' for even length palindrome), then with reverse of first half
    # Use problem 47 (permutation with repeat numbers) to generate the first half
    def generatePalindromes(self, s: str):
        count = Counter(s)
        mid, t = '', [] # t will contain all letters in half of the palindrome permutation
        for c in count:
            t.extend([c]*(count[c]//2))
            if count[c] & 1:
                if mid != '':
                    return []
                else:
                    mid = c
        
        # return [p + mid + p[::-1] for p in set(''.join(it) for it in itertools.permutations(t))] # Use itertools and set to get unique permutations
        return [p + mid + p[::-1] for p in self.permutation(''.join(t))]

    # Generate non-duplicate permutation result, see problem 47 Permutations II
    def permutation(self, s):
        def dfs(s, start, used, build, res):
            if len(build) == len(s):
                res.append(''.join(build))
                return
            for i in range(len(s)):
                if used[i] or (i > 0 and s[i] == s[i-1] and not used[i-1]):
                    continue
                build.append(s[i])
                used[i] = True
                dfs(s, i+1, used, build, res)
                used[i] = False
                build.pop()
        used = [False]*(len(s))
        res = []
        dfs(s, 0, used, [], res)
        return res        

class Test(unittest.TestCase):
    def test_1(self):
        obj = Solution()
        s = "aabb"
        self.assertEqual(set(obj.generatePalindromes(s)), set(["abba", "baab"]))
        s = "ab"
        self.assertEqual(obj.generatePalindromes(s), [])

if __name__ == "__main__":
    unittest.main(exit=False)