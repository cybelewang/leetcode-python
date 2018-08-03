"""
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Note:
The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
"""
# similar problems: 208 Implement Trie

class TrieNode:
    
    def __init__(self, c):
        self.c = c
        self.isLeaf = False
        self.children = {}

class Trie:
    
    def __init__(self):
        self.root = TrieNode('')
        self.root.isLeaf = True
    
    def addWord(self, w):
        node = self.root
        for c in w:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        
        node.isLeaf = True

    def replace(self, w):
        """
        replace w with the shortest root
        """
        node = self.root
        for i, c in enumerate(w):
            if c in node.children:
                node = node.children[c]
                if node.isLeaf:
                    return w[:i+1]
            else:
                break

        return w

class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for w in dict:
            trie.addWord(w)

        return ' '.join(map(trie.replace, sentence.split()))

d = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(Solution().replaceWords(d, sentence))