"""
959 Regions Cut By Slashes

In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.
(Note that backslash characters are escaped, so a \ is represented as "\\".)
Return the number of regions.

Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:

Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
"""
class DSU:
    def __init__(self, N):
        self.root = list(range(N))

    def find(self, x):
        while self.root[x] != x:
            x = self.root[x]
        
        return self.root[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        self.root[rx] = ry

class Solution:
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        N = len(grid)
        dsu = DSU(4*N*N)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                offset = 4*(r*N + c)
                # north: 0, west: 1, south: 3, east: 2
                if val in "/ ":
                    dsu.union(offset + 0, offset + 1)   # connect north and west in a single cell
                    dsu.union(offset + 2, offset + 3)   # connect south and east in a single cell
                if val in "\\ ":
                    dsu.union(offset + 0, offset + 2)   # connect north and east in a single cell
                    dsu.union(offset + 1, offset + 3)   # connect south and west in a single cell
                
                # connect neighboring cells' north and south
                if r > 0:   dsu.union(offset + 0, offset - 4*N + 3)
                #if r < N-1: dsu.union(offset + 3, offset + 4*N + 0)
                
                # connect neighboring cells' east and west
                if c > 0:   dsu.union(offset + 1, offset - 4 + 2)
                #if c < N-1: dsu.union(offset + 2, offset + 4 + 1)
        
        return sum(dsu.find(x) == x for x in range(4*N*N))

grid = [
  "\\/",
  "/\\"
]
print(Solution().regionsBySlashes(grid))