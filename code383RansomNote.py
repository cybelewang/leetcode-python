"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        noteCnt, magCnt = [0]*26, [0]*26
        base = ord('a')
        for c in ransomNote:
            noteCnt[ord(c)-base] += 1
        
        for c in magazine:
            magCnt[ord(c)-base] += 1

        return noteCnt <= magCnt

obj = Solution()
print(obj.canConstruct("a", "b"))# -> false
print(obj.canConstruct("aa", "ab"))# -> false
print(obj.canConstruct("aa", "aab"))# -> true