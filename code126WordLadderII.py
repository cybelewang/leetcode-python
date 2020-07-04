"""
126 Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""
# shortest parth problem of a graph
from collections import deque, defaultdict
class Solution(object):
    # https://www.cnblogs.com/grandyang/p/4548184.html
    # https://leetcode.com/problems/word-ladder-ii/discuss/40434/C%2B%2B-solution-using-standard-BFS-method-no-DFS-or-backtracking
    def findLadders(self, beginWord, endWord, wordList):
        res, wordDict= [], set(wordList)
        paths = deque([[beginWord]])    # outside square brackets are for deque initialization

        level, minLevel = 1, 2**31-1 # current level and min level which has reached endWord
        usedWords = set() # record used words in a single level. One word can be used by different paths as long as these paths have the same length (level here)

        # BFS, but queue paths instead of words
        while paths:
            t = paths.popleft()

            if len(t) > level:
                for w in usedWords:
                    wordDict.remove(w)
                usedWords.clear()
                level = len(t)
                if level > minLevel:
                    break
            
            last = t[-1]
            for newLast in self.G(last, wordDict):
                if newLast not in wordDict:
                    continue
                usedWords.add(newLast)
                nextPath = t[:]
                nextPath.append(newLast)

                if newLast == endWord:
                    res.append(nextPath)
                    minLevel = level
                else:
                    paths.append(nextPath)

        return res

    # BFS processes one level in each while loop, a "standard" way of BFS
    def findLadders2(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:	return []
        
        q, res = deque([[beginWord]]), []
        usedWords = set()   # record all used words in a level
        level, minLevel = 0, 2**31-1
        while q:
            level += 1
            # if minLevel was set to a number other than 2**31-1, that means min length has been found, so length > minLevel can be ignored
            if level > minLevel:
                break
            
            # usedWords must be excluded from wordSet so they cannot be reused by further levels
            for word in usedWords:
                wordSet.remove(word)
            usedWords.clear()

            n = len(q)
            for _ in range(n):
                path = q.popleft()                               
                last = path[-1]

                for newWord in self.G(last, wordSet):
                    if newWord not in wordSet:
                        continue
                    usedWords.add(newWord)
                    newPath = path[:]
                    newPath.append(newWord)
                    if newWord == endWord:
                        res.append(newPath)
                        minLevel = level
                    else:
                        q.append(newPath)

        return res

    # generate the new word by replacing one letter of the word each time
    def G(self, word, wordSet):
        array = list(word)
        for i, letter in enumerate(array):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                array[i] = c
                t = ''.join(array)
                array[i] = letter
                if t != word and t in wordSet:
                    yield t

    def findLadders_WRONG(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        MAX_INT = 2**31 - 1
        alphabet = list(map(chr, range(ord('a'), ord('z')+1)))    # a to z

        res, link = [], defaultdict(list)
        ladder = {} # cache each node's steps
        minSteps = MAX_INT

        # initialize all nodes' steps to MAX_INT except the begin word
        for word in wordList:
            ladder[word] = MAX_INT
        ladder[beginWord] = 0

        # generator for next word
        def G(word):
            for i in range(len(word)):
                for letter in alphabet:
                    array = list(word)
                    array[i] = letter
                    yield ''.join(array)   # generate the new word by replacing one letter of the word each time

        # BFS
        queue = deque([beginWord])
        while queue:
            n = len(queue)
            for _ in range(n):
                word = queue.popleft()
                steps = ladder[word] + 1    # steps of strings which are next level neighbors of word

                if steps > minSteps:    # exit BFS if the endWord has already been found, in this case, do not loop to next level 
                    queue.clear()
                    break
                
                for new_word in G(word):
                    if new_word in ladder and ladder[new_word] >= steps:
                        queue.append(new_word)  # always use the shortest path new_word
                        ladder[new_word] = steps    # always use the least steps
                        
                        # link child node with parent node by using a map
                        link[new_word].append(word)
                        
                        # this is the result in word ladder I
                        if new_word == endWord:
                            minSteps = steps

        # DFS to backtrack the word ladder
        def dfs(build, startWord, link, res):
            word = build[-1]
            if word == startWord:
                res.append(build[::-1])
                return
            for neighbor in link[word]:
                build.append(neighbor)
                dfs(build, startWord, link, res)
                build.pop()

        # build list by back tracking link
        build = [endWord]
        dfs(build, beginWord, link, res)

        return res


obj = Solution()
beginWord, endWord, wordList = "hit", "cog", ["hot","dot","dog","lot","log","cog"]
#beginWord = "rat"
#endWord = "pen"
#wordList = ["rat","pen","pan","pet","pat","ran"]
#beginWord, endWord, wordList = "red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]
print(obj.findLadders2(beginWord,endWord, wordList))