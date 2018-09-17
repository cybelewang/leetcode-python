"""
3 Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
# similar problems: 159 Longest Substring with At Most K Distinct Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        maxLen = 0
        letterIndex = {}
        for (r, letter) in enumerate(s):
            if letter in letterIndex:
                if letterIndex[letter] >= l:              
                    maxLen = max(maxLen, r-l)
                    l = letterIndex[letter] + 1
            letterIndex[letter] = r
        
        maxLen = max(maxLen, len(s)-l)
        return maxLen

# 2nd round solution on 9/14/2018
class Solution2:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        i = 0
        contains, res = set(), 0
        for j in range(n):
            if s[j] in contains:
                while i < j and s[i] != s[j]:
                    contains.remove(s[i])
                    i += 1
                # skip the same letter
                i += 1
            else:
                contains.add(s[j])
            
            res = max(res, j-i+1)
        
        return res