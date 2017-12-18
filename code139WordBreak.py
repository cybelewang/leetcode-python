"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""
# ask corner case of empty string
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        if n < 1:
            return False

        wordSet = set(wordDict)
        dp = [False]*(n + 1)
        dp[0] = True

        for j in range(1, n+1):
            for i in range(0, j):
                if dp[i] and s[i:j] in wordSet:
                    dp[j] = True
                    break
        
        return dp[n]

obj = Solution()
s = 'leetcode'
dict1 = ['leet', 'code']
print(obj.wordBreak(s, dict1))
