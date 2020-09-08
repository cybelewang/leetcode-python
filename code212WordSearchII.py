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
    
    def __init__(self):
        self.children = {}
        self.isLeaf = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.isLeaf = True

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # the DFS will try to include board[i][j] and see if it forms a valid word
        # then it will recursively search neighboring letters
        # a trick to mark [i][j] has been visited is to change its value to '', because '' is not in any TrieNode's children so '' in node.children will always be False
        def dfs(board, i, j, node, build, res):
            # node: board[i][j]'s parent trie node
            # build: array includes previous letters
            # res: final result set
            if -1<i<self.m and -1<j<self.n:
                c = board[i][j]
                if c in node.children:
                    node = node.children[c]
                    build.append(c)
                    board[i][j] = ''    # change [i][j] to mark 'visited'
                    if node.isLeaf:
                        res.add(''.join(build))
                    
                    # dfs in neighboring characters
                    dfs(board, i-1, j, node, build, res)
                    dfs(board, i+1, j, node, build, res)
                    dfs(board, i, j-1, node, build, res)
                    dfs(board, i, j+1, node, build, res)

                    board[i][j] = build.pop()     # restore [i][j]

        trie = Trie()
        for word in words:
            trie.insert(word)

        self.m, self.n = len(board), len(board[0])    
        build, res = [], set()  # bug fixed: use set to hold result strings. consider board = [['a'],['a']] and words = ['a'], the result should be ['a']
        for i in range(self.m):
            for j in range(self.n):
                dfs(board, i, j, trie.root, build, res)

        return list(res)

# 9/3/2020
class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        if m < 1: return []
        n = len(board[0])
        trie = Trie()
        for word in words: trie.insert(word)
        used = [[False]*n for _ in range(m)]
        res = set()
        def dfs(i, j, build, parent):
            c = board[i][j]
            if c not in parent.children: return
            node = parent.children[c]
            build.append(c)
            used[i][j] = True
            if node.isLeaf: res.add(''.join(build))
            for x, y in (i, j-1), (i-1, j), (i, j+1), (i+1, j):                
                if m > x >= 0 <= y < n and not used[x][y]:
                    dfs(x, y, build, node)
            used[i][j] = False
            build.pop()
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, [], trie.root)
                
        return list(res)

board = [['o','a','a','n'],  ['e','t','a','e'],  ['i','h','k','r'],  ['i','f','l','v']]

words = ["oath","pea","eat","rain"]

obj = Solution()
print(obj.findWords(board, words))