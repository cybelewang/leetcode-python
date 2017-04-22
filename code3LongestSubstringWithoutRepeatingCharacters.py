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