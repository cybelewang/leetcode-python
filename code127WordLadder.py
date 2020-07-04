"""
127 Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""

# Use BFS to find the shortest path. To avoid revisiting the same string, the string will be removed from wordList once visited
# Use iterating a-z to get all neighbor strings and check if they are in wordList
class Solution(object):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        
        queue = [beginWord]
        level = 1

        while len(queue) > 0:
            neighbors = []
            for word in queue:
                if word == endWord:
                    return level
                else:
                    self._findNeighbors(word, neighbors, wordSet)
            
            level += 1
            queue = neighbors

        # transformation not found
        return 0

    def _findNeighbors(self, word, neighbors, wordSet):
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

# 2nd round solution on 9/13/2018, bug fixed
from collections import deque
class Solution2:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)        

        q, level = deque([beginWord]), 0
        while q:
            print(q)
            level += 1
            n = len(q)
            for _ in range(n):
                w = q.popleft()
                if w == endWord:
                    return level
                # bug fixed here: we should not remove w from wordSet here, because w may have been removed
                # take the example in problem description, hot -> [dot, lot1], here dot -> [lot2, dog], lot1 -> [log], here lot1 and lot2 are actually same, just differentiate them
                # When we processed [dot, lot1], we will remove lot1, but before that dot has already added lot2 into queue, so next time when seeing lot2, it will raise key error  
                #wordSet.remove(w)    

                chars = list(w)
                for i in range(len(w)):
                    origin = chars[i]
                    for letter in self.letters:
                        if letter != origin:
                            chars[i] = letter
                            transformed = ''.join(chars)
                            if transformed in wordSet:
                                q.append(transformed)
                                wordSet.remove(transformed)
                            chars[i] = origin
                
        return 0


    def ladderLength2(self, beginWord, endWord, wordList):
        # generator for the next mutating word
        def G(s, wordSet):
            letters = list(s)
            for i, letter in enumerate(letters):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    letters[i] = c
                    t = ''.join(letters)
                    letters[i] = letter
                    if t != s and t in wordSet:
                        wordSet.remove(t)
                        yield t
                    
        m = set(wordList)
        if endWord not in m:
            return 0
        q = deque([beginWord])
        level = 0
        while q:
            print(q)
            level += 1
            n = len(q)
            for _ in range(n):
                source = q.popleft()
                for dst in G(source, m):
                    if dst == endWord:
                        return level + 1
                    q.append(dst)
        
        return 0

obj = Solution2()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(obj.ladderLength2(beginWord,endWord, wordList))