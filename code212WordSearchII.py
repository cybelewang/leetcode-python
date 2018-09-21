"""
212 Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.
click to show hint.

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.

"""
class TrieNode:
    
    def __init__(self, c):
        self.c = c
        self.children = {}
        self.isLeaf = False

    def exists(self, c):
        return c in self.children

class Trie:
    
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        
        node.isLeaf = True

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m = len(board)
        if m < 1:
            return []
        n = len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)

        def _dfs(board, m, n, i, j, node, build, res):
            if -1<i<m and -1<j<n:
                c = board[i][j]
                if c in node.children:
                    build.append(c)
                    board[i][j] = ''    # change [i][j] to mark 'visited'
                    if node.children[c].isLeaf: # bug fixed: change from node.isLeaf to node.children[c].isLeaf because node is upper level TrieNode
                        res.add(''.join(build))
                    
                    # dfs in neighboring characters
                    _dfs(board, m, n, i-1, j, node.children[c], build, res)
                    _dfs(board, m, n, i+1, j, node.children[c], build, res)
                    _dfs(board, m, n, i, j-1, node.children[c], build, res)
                    _dfs(board, m, n, i, j+1, node.children[c], build, res)

                    board[i][j] = c     # restore [i][j]
                    build.pop()
            
        build, res = [], set()  # bug fixed: use set to hold result strings. consider board = [['a'],['a']] and words = ['a'], the result should be ['a']
        for i in range(m):
            for j in range(n):
                _dfs(board, m, n, i, j, trie.root, build, res)

        return list(res)

board = [['o','a','a','n'],  ['e','t','a','e'],  ['i','h','k','r'],  ['i','f','l','v']]

words = ["oath","pea","eat","rain"]

obj = Solution()
print(obj.findWords(board, words))