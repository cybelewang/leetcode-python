"""
211 Add and Search Word - Data structure design

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
import unittest
class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isLeaf = False


class WordDictionary:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    # assumes word is not empty
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        
        node.isLeaf = True

    # BFS
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        queue = deque()
        queue.append(self.root)
        for c in word:
            if not queue: return False
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
        
        return any(node for node in queue if node.isLeaf)

    # DFS
    def search2(self, word):
        def helper(word, start, node):
            if start == len(word):
                return node.isLeaf
            c = word[start]
            if c != '.':
                if c in node.children:
                    return helper(word, start+1, node.children[c])
                else:
                    return False
            else: # c == '.'
                return any(helper(word, start + 1, child) for child in node.children.values()) # bug fixed: use node.children.values(), not node.children
        # main
        return helper(word, 0, self.root)

# Your WordDictionary object will be instantiated and called as such:
class Test(unittest.TestCase):
    def test_1(self):
        obj = WordDictionary()
        obj.addWord("bad")
        obj.addWord("dad")
        obj.addWord("mad")
        self.assertEqual(obj.search2("pad"), False) # -> false
        self.assertEqual(obj.search2("bad"), True)# -> true
        self.assertEqual(obj.search2("ba"), False)# -> false
        self.assertEqual(obj.search2(".ad"), True)# -> true
        self.assertEqual(obj.search2("b.."), True)# -> true
# param_2 = obj.search(word)

if __name__ == "__main__":
    unittest.main(exit = False)