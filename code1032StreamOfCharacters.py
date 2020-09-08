"""
1032 Stream of Characters

Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist

Note:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.
"""
# Trie solution by putting reversed word into Trie
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.isLeaf = False
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode() 
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isLeaf = True
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.letters = []

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        node = self.trie.root
        for c in reversed(self.letters):
            node = node.children.get(c, None)
            if node and node.isLeaf:
                return True
            elif node is None:
                break
        
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)