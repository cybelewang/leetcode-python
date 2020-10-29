"""
694 Number of Distinct Islands

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""
class Solution:
    # encode island to a string
    # 's' is the starting cell
    # 'l', 'r', 'u', 'd' are directions
    # 'b' is the finishing symbol, without it, we may get same string as in below example
    # eg:              1 1 1   and    1 1 0
    #                  0 1 0          0 1 1
    # with b:          rdbr           rdr
    # without b:       rdr            rdr    
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def explore(i, j, mark, build):
            nonlocal m, n
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            build.append(mark)
            explore(i, j-1, 'l', build)
            explore(i-1, j, 'u', build)
            explore(i, j+1, 'r', build)
            explore(i+1, j, 'd', build)
            build.append('b')
        
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    shape = []
                    explore(i, j, 's', shape)
                    if shape:
                        seen.add(''.join(shape))
        #print(seen)
        return len(seen)