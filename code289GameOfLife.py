"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

# encode the next live state, current live state into the integer, such as |next live state|current live state|
# 2nd round just keep the next live state
# caution: this solution simply add all 8 neighbors, if you want to cache bottom neighbors for next row's top use, be careful of the corner neighbors since they may be added twice
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                top = 0
                if i > 0:
                    for k in range(max(0, j-1), j+1):
                        top += board[i-1][k] % 2

                left = 0
                if j > 0:
                    for k in range(i, min(i+2, m)):
                        left += board[k][j-1] % 2
                
                bottom = 0
                if i < m-1:
                    for k in range(j, min(j+2, n)):
                        bottom += board[i+1][k] % 2
                
                right = 0
                if j < n-1:
                    for k in range(max(0, i-1), i+1):
                        right += board[k][j+1] % 2
                
                # number of live neighbors
                neighbors = top + left + bottom + right

                # next live state
                live = 0
                if neighbors == 3 or (board[i][j] == 1 and neighbors == 2):
                    live = 1
                
                # encode next live state
                board[i][j] += live*2

        # second round to recover the next live state
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
        
test_matrix = [[1,1,1],[1,1,1],[1,1,1]]
obj = Solution()
obj.gameOfLife(test_matrix)
print(test_matrix)