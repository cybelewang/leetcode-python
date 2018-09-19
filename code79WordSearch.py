"""
79 Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
class Solution(object):
    def _dfs(self, board, used, row, col, word, i):
        """
        row, col: search neighboring cells of [row][col]
        i: index of the character in word to be searched
        """
        if i >= len(word):
            return True

        res = False
        neighbors = [(row-1, col), (row, col + 1), (row + 1, col), (row, col - 1)]  # top, right, bottom, left
        for index in neighbors:
            if -1 < index[0] < len(board) and -1 < index[1] < len(board[0]):
                if board[index[0]][index[1]] == word[i] and not used[index[0]][index[1]]:
                    used[index[0]][index[1]] = True
                    res = res or self._dfs(board, used, index[0], index[1], word, i + 1)
                    used[index[0]][index[1]] = False
        return res

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # what about None?
        if not board or not board[0]:
            if not word:
                return True
            else:
                return False
        else:
            if not word:
                return False

        m, n = len(board), len(board[0])
        used = [[False for j in range(n)] for i in range(m)]
        res = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    used[i][j] = True
                    res = res or self._dfs(board, used, i, j, word, 1)
                    used[i][j] = False
        
        return res

obj = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

test_words = ['', ' ', 'ABCCED', 'SEE', 'ABCB']
for word in test_words:
    print(word, end = ' -> ')
    print(obj.exist(board, word))

        