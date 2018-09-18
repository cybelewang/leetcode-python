"""
36 Valid Sodoku

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
"""
class Solution(object):
    def isRowValid(self, board):
        record = {}        
        for row in board: # row type: List[str]
            record.clear()
            for e in row:
                if e != '.':
                    if e not in record:
                        record[e] = True
                    else:
                        return False

        return True
    
    def isColumnValid(self, board):
        record = {}
        for i in range(len(board[0])):
            record.clear()
            for row in board:
                e = row[i]
                if e != '.':
                    if e not in record:
                        record[e] = True
                    else:
                        return False
        
        return True

    def isSubBoxValid(self, board):
                

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """