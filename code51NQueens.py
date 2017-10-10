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
class Solution(object):
    def _toResult(self, used, res):
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

    def _allowed(self, used, i, j, n):
        # check rows
        if any(used[i]):
            return False
        for x in range(n):
            if used[x][j]:
                return False
            # check diagnol
            y1 = x + j - i
            y2 = j + i - x
            if 0 <= y1 < n and used[x][y1]:
                return False
            if 0 <= y2 < n and used[x][y2]:
                return False
        
        return True                

    def _NQueens(self, n, i, used, res):
        # i is the row to insert a Queen
        if i == n:
            self._toResult(used, res)
        else:
            bFound = False        
            for j in range(n):
                if self._allowed(used, i, j, n):
                    bFound = True   # Found a proper place to place the Queen
                    used[i][j] = True
                    self._NQueens(n, i + 1, used, res)
                    used[i][j] = False
            if not bFound: # iterating all columns and cannot find a place for the Queen, just return
                return
        
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1:
            return []
        
        used = [[False for i in range(n)] for j in range(n)]
        res = []
        self._NQueens(n, 0, used, res)   

        return res

obj = Solution()
res = obj.solveNQueens(4)
print(res)