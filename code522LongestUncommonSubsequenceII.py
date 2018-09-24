"""
522 Longest Uncommon Subsequence II

Given a list of strings, you need to find the longest uncommon subsequence among them. 
The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. 
Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. 
If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3
Note:

All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].
"""
# first move all duplicated strings to another set, we cannot discard them because the remaining unique str could be subsequence of these duplicated strs
# then iterate all unique strs, and check if they are any subsequence of the duplicated strs
from collections import Counter
class Solution:
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = Counter(strs)
        unique = set(count.keys())
        duplicate = set()

        # any duplicated string will not be LUS
        for s in count.keys():
            if count[s] > 1:
                unique.remove(s)
                duplicate.add(s)
        
        res = -1
        for s in unique:
            # pitfall fixed: must compare with those duplicated string
            for d in duplicate:
                if self.issubsequence(s, d):
                    break
            else:
                res = max(res, len(s))

        return res

    def issubsequence(self, s1, s2):
        if len(s1) > len(s2):
            return False
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s2[j] == s1[i]:
                i += 1
            j += 1

        return i == len(s1)

strs = ["aaa", "aaa", "aa"]
obj = Solution()
print(obj.findLUSlength(strs))
