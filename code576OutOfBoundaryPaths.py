"""
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, 
you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). 
However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. 
The answer may be very large, return it after mod 10^9 + 7.

Example 1:
Input:m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:
Input:m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

Note:
Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].
"""
class Solution:
    # my own solution
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        M = 1000000007
        # ask about if i, j are valid

        # occurrence[i][j] is the times that ball appears in this position
        occurrence = [[0]*n for _ in range(m)]
        occurrence[i][j] = 1

        # a set with all possible current positions
        current = {(i,j)}
        
        neighbors = [[0,-1], [-1,0], [0,1], [1, 0]] # left, above, right, below
        for _ in range(N-1):
            next = set()
            for i, j in current:                
                for dx, dy in neighbors:
                    x, y = i + dx, j + dy   # new position
                    if -1 < x < m and -1 < y < n:
                        occurrence[x][y] = (occurrence[x][y] + 1) % M   # add 1 to the new valid position
                        next.add((x,y))
            current = next
        
        # iterate all boarder cells and calculate the paths
        res = 0
        # top
        res = (res + sum(occurrence[0])) % M
        # bottom
        res = (res + sum(occurrence[m-1])) % M
        # left and right
        res = (res + sum([row[0] + row[n-1] for row in occurrence])) % M

        return res

print(Solution().findPaths(50,50,50,0,0))