"""
320 Generalized Abbreviation

Write a function to generate the generalized abbreviations of a word.

Example:

Given word = "word", return the following list (order does not matter):

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""
class Solution:
    # https://www.cnblogs.com/grandyang/p/5261569.html
    def generateAbbreviations(self, word):
        n = len(word)
        res = [str(n) if n > 0 else ""]
        for i in range(n):
            for a in self.generateAbbreviations(word[i+1:]):
                left = str(i) if i > 0 else ""
                res.append(left + word[i] + a)
        
        return res
    
    # sequential recurrence by left appending the first letter of word to the result of word[1:]
    # be cautious when the result of word[1:] starts with digits, need to add that number by 1
    def generateAbbreviations3(self, word):
        if not word: return [""]
        # return a list of abbreviations
        if len(word) == 1: return [word, '1']
        l, res = word[0], []
        for r in self.generateAbbreviations(word[1:]):
            res.append(l + r)
            if r[0].isdigit():
                # find the starting number
                k = 0
                while k < len(r) and r[k].isdigit():
                    k += 1
                num, remain = int(r[:k]), r[k:]
                res.append(str(1+num)+remain)
            else:
                res.append('1' + r)
        return res    
     
    def generateAbbreviations2(self, word):
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

    # classic backtracking
    def generateAbbreviations(self, word: str) -> List[str]:
        # "w" -> ['1', 'w']
        # "wo" -> ['2', 'w1', '1o', 'wo']
        # "wor" -> ['3', 'w2', '1o1', 'wo1', '2r', 'w1r', '1or', 'wor']
        def helper(start, build, res):
            if start == len(word):
                res[:] = build[:]
                return
            next_build = []
            for pre in build:
                if pre[-1].isdigit():
                    i = len(pre) - 1
                    while i > -1 and pre[i].isdigit():
                        i -= 1
                    i += 1
                    next_build.append(pre[:i] + str(int(pre[i:]) + 1))
                else:
                    next_build.append(pre + '1')
                next_build.append(pre + word[start])
            helper(start+1, next_build, res)
            
        if word == '':
            return ['']
        res = []
        helper(1, ['1', word[0]], res)
        return res

print(Solution().generateAbbreviations3("word"))