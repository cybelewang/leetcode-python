"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. 
If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""
class Solution:
    # more efficient, no sorting, https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/discuss/99588/Short-Java-Solutions-Sorting-Dictionary-and-Without-Sorting
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        res = ''
        for s1 in d:
            i, j = 0, 0
            while i < len(s1) and j < len(s):
                if s[j] == s1[i]:
                    i += 1
                j += 1
            if i == len(s1):
                if i > len(res) or (i == len(res) and s1 < res):
                    res = s1
        
        return res
                
    # my own brute force solution
    # first sort d based on the length and lexicographical order
    # second iterate sorted d and find the first string which is subsequence of s
    def findLongestWord2(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key = lambda x: (-len(x), x))
        for s1 in d:
            if self.isSubsequence(s1, s):
                return s1
        else:
            return ''

    def isSubsequence(self, s1, s2):
        if len(s1) > len(s2):
            return False

        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s2[j] == s1[i]:
                i += 1
            j += 1

        return i == len(s1)

s = "bab"
d = ["ba","ab","a","b"]
print(Solution().findLongestWord(s, d))