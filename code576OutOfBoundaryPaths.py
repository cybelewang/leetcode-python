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
    # help from http://www.cnblogs.com/grandyang/p/6927921.html
    # key is the definition of DP array
    def findPaths(self, m, n, N, i, j):
        M = 1000000007

        dp = [[[0]*n for _ in range(m)] for _ in range(N+1)]  # dp[k][i][j] is the number of paths out of boundary starting from cell [i][j] after k steps

        for k in range(1, N+1):
            for x in range(m):
                for y in range(n):
                    v1 = 1 if y == 0 else dp[k-1][x][y-1]  # from left
                    v2 = 1 if x == 0 else dp[k-1][x-1][y]  # from above
                    v3 = 1 if y == n-1 else dp[k-1][x][y+1]    # from right
                    v4 = 1 if x == m-1 else dp[k-1][x+1][y]    # from below
                    dp[k][x][y] = (v1 + v2 + v3 + v4) % M
        
        return dp[N][i][j]

    # BFS solution, corrected from findPaths_WRONG
    # key is to use a new 2-D matrix to hold the number of appearances in [i][j]
    def findPaths2(self, m, n, N, i, j):
        M = 1000000007
        neighbors = [[0, -1], [-1, 0], [0,1], [1, 0]]
        q = {(i, j)}    # holds the positions of ball in last move

        pre = [[0]*n for _ in range(m)] # holds the number of appearances of ball in last move in [i][j]
        pre[i][j] = 1
        res = 0

        for _ in range(N):
            cur = [[0]*n for _ in range(m)] # initialize a new 2-D matrix to calculate the number of appearances of ball after 1-step move
            next_ = set()   # initialize a new set to hold the new positions after 1-step move
            for i, j in q:
                for dx, dy in neighbors:
                    x, y = i+dx, j+dy
                    if -1 < x < m and -1 < y < n:   # within boundary, update cur and next_
                        cur[x][y] += pre[i][j]
                        next_.add((x,y))
                    else:
                        res = (res + pre[i][j]) % M # out of boundary, update res
            
            # update pre and q
            pre = cur
            q = next_

        return res
         
    # my own solution, wrong on DP derivation
    def findPaths_WRONG(self, m, n, N, i, j):
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
            next_ = set()
            for i, j in current:                
                for dx, dy in neighbors:
                    x, y = i + dx, j + dy   # new position
                    if -1 < x < m and -1 < y < n:
                        # below is wrong because occurrence[i][j] may not be accumulated at one time, so it doresn't represent the existence just for the last step
                        occurrence[x][y] = (occurrence[i][j] + occurrence[x][y])%M
                        # below is wrong because if occurrence[i][j] > 1, occurrence[x][y] should take all the values from occurrence[i][j]
                        #occurrence[x][y] = (occurrence[x][y] + 1) % M   # add 1 to the new valid position
                        next_.add((x,y))
            current = next_
        
        # iterate all boarder cells and calculate the paths
        res = 0
        # top
        res = (res + sum(occurrence[0])) % M
        # bottom
        res = (res + sum(occurrence[m-1])) % M
        # left and right
        res = (res + sum([row[0] + row[n-1] for row in occurrence])) % M

        return res

print(Solution().findPaths2(2,3,8,1,0))