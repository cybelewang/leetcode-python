"""
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
class Solution(object):
    link = {}   # link adjacent words
    res = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # convert the word list to a set
        wordSet = set(wordList)
        wordSet.add(beginWord)
        wordSet.add(endWord)

        # initially set all graphic nodes' steps to MAX_INT
        MAX_INT = 2**31 - 1
        minSteps = MAX_INT

        queue = [beginWord]
        ladder = {} # cache each node's steps

        # initialize all nodes' steps to MAX_INT except the begin word
        for word in wordSet:
            ladder[word] = MAX_INT
        ladder[beginWord] = 0

        while len(queue) > 0:
            word = queue.pop()
            steps = ladder[word] + 1

            if steps > minSteps:    # what's this?
                break
            
            for i in range(len(word)):
                array = list(word)
                for letter in self.alphabet:
                    array[i] = letter
                    new_word = ''.join(array)   # generate the new word
                    if new_word in ladder:
                        if steps > ladder[new_word]:
                            continue
                        elif steps < ladder[new_word]:
                            queue.append(new_word)
                            ladder[new_word] = steps
                        
                        if new_word in self.link:
                            self.link[new_word].append(word)
                        else:
                            new_list = [word]
                            self.link[new_word] = new_list
                        
                        if new_word == endWord:
                            minSteps = steps

        build = []
        self.backTrace(endWord, beginWord, build)

        return self.res


    def backTrace(self, word, beginWord, build):
        if word == beginWord:
            build.insert(0, beginWord)
            self.res.append(build[:])
            build.remove(beginWord)
            return
        build.insert(0, word)
        if word in self.link:
            for s in self.link[word]:
                self.backTrace(s, beginWord, build)
        build.remove(word)

obj = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(obj.findLadders(beginWord,endWord, wordList))