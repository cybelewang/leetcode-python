"""
52 N Queens II

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""
class Solution(object):
    t = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        used = [[False for i in range(n)] for j in range(n)]
        self._NQueens(n, 0, used)

        return self.t
    
    def _NQueens(self, n, i, used):
        if i == n:
            self.t += 1
        else:
            bFound = False
            for j in range(n):
                if self._allowed(used, n, i, j):
                    bFound = True
                    used[i][j] = True
                    self._NQueens(n, i + 1, used)
                    used[i][j] = False
            if not bFound:
                return

    def _allowed(self, used, n, i, j):
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

obj = Solution()
print(obj.totalNQueens(8))