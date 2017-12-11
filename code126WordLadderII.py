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
# shortest parth problem of a graph
class Solution(object):
    def __init__(self):
        self.link = {}   # current node: parent node
        self.res = []
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # initially set all graphic nodes' steps to MAX_INT
        MAX_INT = 2**31 - 1
        minSteps = MAX_INT

        ladder = {} # cache each node's steps

        # initialize all nodes' steps to MAX_INT except the begin word
        for word in wordList:
            ladder[word] = MAX_INT
        ladder[beginWord] = 0

        queue = [beginWord]
        while len(queue) > 0:
            new_queue = []      # queue for next level
            for word in queue:  # iterate all words in current level queue           
                steps = ladder[word] + 1    # steps of strings which are next level neighbors of word

                if steps > minSteps:    # exit BFS if the endWord has already been found, in this case, do not loop to next level 
                    break
                
                for i in range(len(word)):
                    array = list(word)
                    for letter in self.alphabet:
                        array[i] = letter
                        new_word = ''.join(array)   # generate the new word by replacing one letter of the word each time
                        if new_word in ladder:
                            if steps > ladder[new_word]:
                                continue
                            elif steps < ladder[new_word]:
                                new_queue.append(new_word)  # always use the shortest path new_word
                                ladder[new_word] = steps    # always use the least steps
                            
                            # link child node with parent node by using a map
                            if new_word in self.link:
                                self.link[new_word].append(word)
                            else:
                                new_list = [word]
                                self.link[new_word] = new_list
                            
                            # this is the result in word ladder I
                            if new_word == endWord:
                                minSteps = steps
            # update queue to next level queue
            queue = new_queue

        # build list by back tracking self.link
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
beginWord = "rat"
endWord = "pen"
wordList = ["rat","pen","pan","pet","pat","ran"]
print(obj.findLadders(beginWord,endWord, wordList))