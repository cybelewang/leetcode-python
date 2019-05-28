"""
36 Valid Sodoku

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
"""
class Solution(object):
    # https://www.cnblogs.com/grandyang/p/4421217.html
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        
        m, n = len(board), len(board[0])
        rowFlag = [[False]*n for _ in range(m)]
        colFlag = [[False]*n for _ in range(m)]
        cellFlag = [[False]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if '1' <= board[i][j] <= '9':
                    c = ord(board[i][j]) - ord('1')
                    if rowFlag[i][c] or colFlag[c][j] or cellFlag[3*(i//3) + j//3][c]:
                        return False
                    rowFlag[i][c] = True
                    colFlag[c][j] = True
                    cellFlag[3*(i//3) + j//3][c] = True

        return True