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
    def findLadders(self, beginWord, endWord, wordList):
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
                
                for i in range(len(word)):
                    for letter in alphabet:
                        array = list(word)
                        array[i] = letter
                        new_word = ''.join(array)   # generate the new word by replacing one letter of the word each time
                        if new_word in ladder and ladder[new_word] > steps:
                            queue.append(new_word)  # always use the shortest path new_word
                            ladder[new_word] = steps    # always use the least steps
                            
                            # link child node with parent node by using a map
                            link[new_word].append(word)
                            
                            # this is the result in word ladder I
                            if new_word == endWord:
                                minSteps = steps

        # build list by back tracking link
        build = []
        self.backTrace(endWord, beginWord, link, build, res)

        return res


    def backTrace(self, word, beginWord, link, build, res):
        if word == beginWord:
            build.insert(0, beginWord)
            res.append(build[:])
            build.remove(beginWord)
            return
        build.insert(0, word)
        if word in link:
            for s in link[word]:
                self.backTrace(s, beginWord, link, build, res)
        build.remove(word)

obj = Solution()
beginWord = "rat"
endWord = "pen"
wordList = ["rat","pen","pan","pet","pat","ran"]
print(obj.findLadders(beginWord,endWord, wordList))