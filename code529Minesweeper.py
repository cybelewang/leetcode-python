"""
529 Minesweeper

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
Example 1:
Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:
Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Note:
The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.
"""
import copy
class Solution:
    # my own dfs solution
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        neighbors = [[0,-1], [-1,-1], [-1, 0],[-1, 1], [0, 1],[1,1], [1, 0],[1,-1]]

        # main
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board

        m, n = len(board), len(board[0])
        count = [[0]*n for _ in range(m)]

        # assign mineral count to all cells
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'M':
                    count[i][j] = 100   # set the mineral itself to a very large count
                    for dx, dy in neighbors:
                        x, y = i + dx, j + dy
                        if -1 < x < m and -1 < y < n:
                            count[x][y] += 1
       
        # dfs definition                    
        def dfs(board, i, j, m, n):
            """
            i, j: indices of selected index
            m, n: size of board
            """
            if -1 < i < m and -1 < j < n:
                cur = board[i][j]
                if cur == 'E':
                    if count[i][j] == 0:
                        board[i][j] = 'B'
                        for dx, dy in neighbors:
                            x, y = i + dx, j + dy
                            dfs(board, x, y, m, n)
                    else:
                        board[i][j] = str(count[i][j])

        dfs(board, click[0], click[1], m, n)

        return board

    # another DFS solution by counting mines during DFS
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        res = copy.deepcopy(board)
        def reveal(i, j, board, res):
            if m > i >= 0 <= j < n:
                if res[i][j] == 'E': # bug fixed: should use res, not board
                    count = 0
                    for x, y in (i, j-1), (i-1, j-1), (i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1, j), (i+1, j-1):
                        if m > x >= 0 <= y < n:
                            if board[x][y] == 'M':
                                count += 1
                    if count > 0:
                        res[i][j] = str(count)
                    else:
                        res[i][j] = 'B'
                        for x, y in (i, j-1), (i-1, j-1), (i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1, j), (i+1, j-1):
                            reveal(x, y, board, res)
        x0, y0 = click
        if board[x0][y0] == 'M':
            res[x0][y0] = 'X'
            return res
        reveal(x0, y0, board, res)
        return res
                            
board = [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
print(Solution().updateBoard(board, (1, 2)))