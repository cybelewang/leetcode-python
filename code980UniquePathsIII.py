"""
980 Unique Paths III

On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

Note:
1 <= grid.length * grid[0].length <= 20
"""
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        r1, c1, r2, c2, empty = None, None, None, None, 0
        # 1st pass grid and save start, end positions, also count empty spaces
        # note that we set end cell to 0 to allow it to be reached
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    r1, c1 = r, c
                elif grid[r][c] == 2:
                    r2, c2 = r, c
                    grid[r][c] = 0
                elif grid[r][c] == 0:
                    empty += 1
        # DFS function that returns number of paths which walks over all empty spaces
        def helper(r, c, remain):
            if remain < 0: return 0
            if (r, c) == (r2, c2):
                return remain == 0
            paths = 0
            for x, y in (r, c-1), (r-1, c), (r, c+1), (r+1, c):
                if M > x >= 0 <= y < N and grid[x][y] == 0:
                    grid[x][y] = 3 # a temporary value which marks this cell has been visited
                    paths += helper(x, y, remain - 1)
                    grid[x][y] = 0 # restore the value of (x, y)
            return paths
        
        return helper(r1, c1, empty + 1) # bug fixed: we must add 1 to empty because end cell has been changed to empty