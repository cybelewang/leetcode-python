"""
320 Generalized Abbreviation

Write a function to generate the generalized abbreviations of a word.

Example:

Given word = "word", return the following list (order does not matter):

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""
class Solution:
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: list[str]
        """
        def dfs(word, prefix, start, cnt, res):
            """
            start: start index in word
            cnt: count of previously skipped letters
            """
            if start == len(word):
                res.append(prefix + (str(cnt) if cnt > 0 else ''))
                return
            
            #case 1: use word[start] as letter
            dfs(word, prefix+(str(cnt) if cnt > 0 else '')+word[start], start+1, 0, res)
            #case 2: skip word[start]
            dfs(word, prefix, start+1, cnt+1, res)
        
        #main
        res = []
        dfs(word, "", 0, 0, res)

        return res

print(Solution().generateAbbreviations("word"))