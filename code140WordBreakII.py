"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

"""
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        if n < 1:
            return []

        wordSet = set(wordDict)
                
        res = []
        self._dfs(s, wordSet, 0, [], res)

        return res

    def _dfs(self, s, wordSet, i, build, res):
        n = len(s)
        if i == n:
            res.append(' '.join(build))
            return
        
        for j in range(i+1, n+1):# bug fixed: should be n + 1, not n
            if s[i:j] in wordSet:
                build.append(s[i:j])
                self._dfs(s, wordSet, j, build, res)
                build.pop()
        
    
obj = Solution()
s = "catsanddog"
d = ["cat", "cats", "and", "sand", "dog"]
print(obj.wordBreak(s, d))
