"""
348 Design Tic-Tac-Toe

Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | | // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | | // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | | // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| | // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| | // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| | // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| | // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?

Hint:

Could you trade extra space such that move() operation can be done in O(1)?
You need two arrays: int rows[n], int cols[n], plus two variables: diagonal, anti_diagonal.
"""
class TicTacToe:
    def __init__(self, n):
        self.N = n
        self.rows = [0]*n   # self.rows[i] is the count difference between player 1 and 2 in row i
        self.cols = [0]*n   # self.cols[i] is the count difference between player 1 and 2 in col i
        self.diagonal = 0   # count difference between player 1 and 2 in diagonal
        self.anti_diagonal = 0    # count difference between player 1 and 2 in anti-diagonal

    def move(self, row, col, player):
        value = 3 - 2*player # 3 - 2*player: 1 for player 1, -1 for player 2
        self.rows[row] += value 
        self.cols[col] += value
        if row == col:
            self.diagonal += value
        if row + col == self.N - 1:
            self.anti_diagonal += value
        
        if self.N * value in (self.rows[row], self.cols[col], self.diagonal, self.anti_diagonal):
            return player
        else:
            return 0

game = TicTacToe(3)
print(game.move(0, 0, 1))   # expect 0
print(game.move(0, 2, 2))   # expect 0
print(game.move(2, 2, 1))   # expect 0
print(game.move(1, 1, 2))   # expect 0
print(game.move(2, 0, 1))   # expect 0
print(game.move(1, 0, 2))   # expect 0
print(game.move(2, 1, 1))   # expect 1