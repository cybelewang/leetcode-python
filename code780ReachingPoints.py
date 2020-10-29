"""
780 Reaching Points

A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:

sx, sy, tx, ty will all be integers in the range [1, 10^9].
"""
class Solution:
    # Brutal-force backward solution
    # if x > y, update x to x - y
    # if x < y, update y to y - x
    # This will cause TLE for test case like (1, 1, 1000000000, 1)
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if tx > ty:
                tx = tx-ty
            else:
                ty = ty-tx
        return tx == sx and ty == sy

    # one thing we found is that if tx > ty > sy, then we can use tx = tx % ty to replace while tx > ty: tx -= ty
    def reachingPoints2(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        # now check if we reduce (tx, ty) to (sx, sy+k*sx) or (sx+k*sy, sy)
        return (tx == sx and sy <= ty and (ty - sy) % tx == 0) or \
    (ty == sy and sx <= tx and (tx - sx) % ty == 0)