"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""
# The difference from Trie is that we use a queue to store potentially matching TrieNodes when searching because of '.'
# Finally we check if there is a TrieNode in queue and its isLeaf is True

from collections import deque

class TrieNode:
    
    def __init__(self, c):
        self.c = c
        self.children = {}
        self.isLeaf = False


class WordDictionary:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')
        

    # assumes word is not empty
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        
        node.isLeaf = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        queue = deque()
        queue.append(self.root)
        for c in word:
            n = len(queue)
            if c != '.':
                for i in range(n):
                    node = queue.popleft()
                    if c in node.children:
                        queue.append(node.children[c])
            else:
                for i in range(n):
                    node = queue.popleft()
                    queue.extend(node.children.values())
        
        for node in queue:
            if node.isLeaf:
                return True
        
        return False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))# -> false
print(obj.search("bad"))# -> true
print(obj.search("ba"))# -> false
print(obj.search(".ad"))# -> true
print(obj.search("b.."))# -> true
# param_2 = obj.search(word)