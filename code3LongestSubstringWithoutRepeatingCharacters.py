class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        maxLen = 1
        letterIndex = {}
        for (r, letter) in enumerate(s):
            if letter in letterIndex:
                if letterIndex[letter] >= l:
                    letterIndex[letter] = r
                    l = l + 1
                    maxLen = max(maxLen, r-l)
            else:
                letterIndex[letter] = r
        
        maxLen = max(maxLen, len(s)-l)
        return maxLen