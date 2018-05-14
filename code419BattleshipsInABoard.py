"""
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
"""
class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # when seeing a "X", see if its above or left is "X", if so, this means "X" is part of ship, if not, this means "X" is head of the ship, count 1
        if not board:
            return 0

        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                count += (board[i][j] == 'X') and ((i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'))

        return count

#board = [['X','.','.','X'], ['.','.','.','X'],['.','.','.','X']]
board = ['X','.','X']
obj = Solution()
print(obj.countBattleships(board))