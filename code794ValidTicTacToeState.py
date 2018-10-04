"""
794 Valid Tic-Tac-Toe State

A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
Note:

board is a length-3 array of strings, where each string board[i] has length 3.
Each board[i][j] is a character in the set {" ", "X", "O"}.
"""

# 1. if player 1 wins, then player 2 must not win, and count('X') == count('O') + 1
# 2. if player 2 wins, then player 1 must not win, and count('X') == count('O')
# 3. if no player wins, then count('X') == count('O') + 1 or count('X') == count('O')
class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        countX = sum(row.count('X') for row in board)
        countO = sum(row.count('O') for row in board)
        
        r0, r1, r2 = board
        states = set([r0, r1, r2, r0[0]+r1[0]+r2[0], r0[1]+r1[1]+r2[1], r0[2]+r1[2]+r2[2], r0[0]+r1[1]+r2[2], r0[2]+r1[1]+r2[0]])
        win1 = "XXX" in states
        win2 = "OOO" in states

        if win1 and win2:
            return False
        elif win1:
            return countX == countO + 1
        elif win2:
            return countX == countO
        else:
            return countX in (countO, countO + 1)

board = ["O  ", "   ", " X "]
print(Solution().validTicTacToe(board))