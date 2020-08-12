"""
1197 Minimum Knight Moves

In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.
 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5] 

Constraints:

|x| + |y| <= 300
"""
class Solution:
    # https://leetcode.com/problems/minimum-knight-moves/discuss/386992/get-rid-of-TLE-for-python-BFS
    # BFS solution
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        dirs = [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1), (-1,-2),(-2,-1)]
        q = deque([(0, 0, 0)])
        seen = {(0, 0),}
        x, y = abs(x), abs(y)
        while q:
            length = len(q)
            for _ in range(length):
                i, j, d = q.popleft()
                for dx, dy in dirs:
                    r, c = i+dx, j+dy
                    if r == x and c == y:
                        return d + 1
                    if r > -4 and c > -4 and (r, c) not in seen:
                        q.append((r, c, d+1))
                        seen.add((r, c))
        