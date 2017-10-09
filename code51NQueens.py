"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""
def _toResult(used, res):
    sub = []
    for row in used:
        build = ''
        for e in row:
            if e:
                build += 'Q'
            else:
                build += '.'
        sub.append(build)
    res.append(sub)

def _allowed(used, i, j):
    # check rows
    QueueInRow = any(used[i][:])
    # check columns
    QueueInCol = any(used[:][j])                
    # check diagnol
    

def _NQueens(n, i, used, res):
    # i is the row to insert a Queen
    if i == n:
        _toResult(used, res)
    else:
        bFound = False        
        for j in range(n):
            if _allowed(used, i, j):
                bFound = True
                used[i][j] = True
                _NQueens(n, i + 1, used, res)
                used[i][j] = False
        if not bFound:
            return
    
def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    if n < 1:
        return []
    
    used = [[False for i in range(n)] for j in range(n)]
    res = []
    _NQueens(n, 0, used, res)   

    return res