import unittest
def checkWinState(grid):
    """
    return True if 'X' or 'O' wins in grid
    time complexity O(m*n), space complexity O(m+n)
    """
    m, n = len(grid), len(grid[0])              # number of rows, number of columns
    col_cnt = [[0]*n, [0]*n]                    # players' number of vertical continuous markers from grid[cur row][j] to grid[0][j]
    diag_cnt = [[0]*(m+n-1), [0]*(m+n-1)]       # players' number of diagonal continuous markers from top left to current cell 
    anti_diag_cnt = [[0]*(m+n-1), [0]*(m+n-1)]  # players' number of diagonal continuous markers from top right to current cell 

    for i in range(m):
        row_cnt = [0, 0] # players' continuous Xs and Os in this row
        for j in range(n):
            if grid[i][j] in ('X', 'O'):
                player, other = (0, 1) if grid[i][j] == 'X' else (1, 0)
                # check row
                row_cnt[player], row_cnt[other] = row_cnt[player] + 1, 0
                if row_cnt[player] > 2:
                    return True
                # check column
                col_cnt[player][j], col_cnt[other][j] = col_cnt[player][j] + 1, 0
                if col_cnt[player][j] > 2:
                    return True
                # check diagonal
                index = n - 1 + i - j
                diag_cnt[player][index], diag_cnt[other][index] = diag_cnt[player][index] + 1, 0
                if diag_cnt[player][index] > 2:
                    return True
                # check anti-diagonal
                index = i + j
                anti_diag_cnt[player][index], anti_diag_cnt[other][index] = anti_diag_cnt[player][index] + 1, 0
                if anti_diag_cnt[player][index] > 2:
                    return True
            else:
                # 'B', 'E'
                row_cnt = [0, 0]
                col_cnt[0][j] = col_cnt[1][j] = 0
                index = n - 1 + i - j
                diag_cnt[0][index] = diag_cnt[1][index] = 0
                anti_diag_cnt[0][i+j] = anti_diag_cnt[1][i+j] = 0
    
    return False

def canFill(grid):
    """
    Check if the given grid's empty cells can be filled with X or O without causing a win state
    time complexity O(m*n*2^E), E is the number of empty cells
    """
    m, n = len(grid), len(grid[0])
    if checkWinState(grid):
        return False
    unfilled = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 'E']
    remain = len(unfilled)
    # DFS function to check if grid can be filled 
    def helper(unfilled, remain):
        if remain == 0:
            print(grid) # print the filled board
            return True
        for i, j in unfilled:
            if grid[i][j] != 'E':
                continue
            for marker in ('X', 'O'):
                grid[i][j] = marker
                if not checkWinState(grid) and helper(unfilled, remain - 1):
                    return True
                grid[i][j] = 'E'
        return False

    return helper(unfilled, remain)

class Test(unittest.TestCase):
    def test_1(self):
        # test when given board already in win state
        test_grid = [['X', 'O'],
                     ['X', 'B'],
                     ['X', 'O']]  
        self.assertEqual(canFill(test_grid), False) 

    def test_2(self):
        # test when given board not in win state but no empty cells
        test_grid = [['X', 'O'],
                     ['O', 'B'],
                     ['X', 'O']]  
        self.assertEqual(canFill(test_grid), True) 

    def test_3(self):
        # test when given board has empty cell and can be filled
        test_grid = [['X', 'O'],
                     ['E', 'B'],
                     ['X', 'O']]  
        self.assertEqual(canFill(test_grid), True) 

    def test_4(self):
        # test when given board has empty cells and cannot be filled
        test_grid = [['E', 'X', 'X', 'O'],
                     ['X', 'B', 'E', 'O'],
                     ['X', 'O', 'X', 'B']]  
        self.assertEqual(canFill(test_grid), False)

    def test_5(self):
        # test when given board has empty cells and can be filled
        test_grid = [['E', 'X', 'X', 'O', 'B'],
                     ['X', 'B', 'E', 'E', 'O'],
                     ['E', 'E', 'B', 'O', 'B'],
                     ['X', 'O', 'X', 'B', 'E'],
                     ['X', 'B', 'E', 'O', 'E']]  

        self.assertEqual(canFill(test_grid), True)     

if __name__ == '__main__':
    unittest.main(exit = False)