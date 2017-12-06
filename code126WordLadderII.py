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
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        if beginWord in wordSet:
            wordSet.remove(beginWord)

        queue = [beginWord]
        res, build = [], [beginWord]
        bFound = False

        while len(queue) > 0 and not bFound:
            neighbors = []
            for word in queue:
                self._findNeighbors(word, neighbors, build, res, wordSet)

            queue = neighbors
            bFound = True if len(res) > 0

        return res


    def _findNeighbors(self, word, neighbors, build, res, wordSet):
        """
        :type word: str
        :type neighbors: list
        :type wordSet: set
        """      
        for i in range(len(word)):
            array = list(word)
            for letter in self.alphabet:
                array[i] = letter
                candidate = ''.join(array)
                if candidate in wordSet:
                    neighbors.append(candidate)
                    wordSet.remove(candidate)