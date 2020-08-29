"""
139 Word Break

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
    # DP solution, time O(N^3), space O(N)
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for j in range(1, n+1):
            for i in range(j):
                if s[i:j] in wordSet:
                    dp[j] |= dp[i]
        #print(dp)
        return dp[-1]

    # DFS solution with map
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(s, wordSet, start, mem):
            if start in mem:
                return mem[start]
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordSet and helper(s, wordSet, end, mem):
                    mem[start] = True
                    return True
            mem[start] = False
            return False
        
        # main
        wordSet = set(wordDict)
        mem = {len(s): True}
        return helper(s, wordSet, 0, mem)

obj = Solution()
s = 'leetcode'
dict1 = ['leet', 'code']
print(obj.wordBreak(s, dict1))
