"""
208 Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""
class TrieNode:
    
    def __init__(self):
        self.children = {}  # key= child character, value=child TrieNode's pointer
        self.isLeaf = False # mark the end of word

class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
   

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            node.children.setdefault(c, TrieNode())
            node = node.children[c]

        node.isLeaf = True  # mark the end of word


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        
        return node.isLeaf


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
obj.insert('abc')
print(obj.search('abc'))
print(obj.search('ab'))
print(obj.startsWith('a'))