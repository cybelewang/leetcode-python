"""
1240 Tiling a Rectangle with the Fewest Squares

Given a rectangle of size n x m, find the minimum number of integer-sided squares that tile the rectangle.

Example 1:
Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)

Example 2:
Input: n = 5, m = 8
Output: 5

Example 3:
Input: n = 11, m = 13
Output: 6

Constraints:
1 <= n <= 13
1 <= m <= 13
"""
class Solution:
    # https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/discuss/414260/8ms-Memorized-Backtrack-Solution-without-special-case!
    def tilingRectangle(self, n, m):
        # n: number of rows
        # m: number of columns
        if m > n:
            m, n = n, m
        INF = n*m

        @lru_cache(None)
        def dp(state):
            # state: tuple of size m with element indicates each column's filled height, use tuple for cache
            # return: min number of squares to fill up the state

            # base case: all columns have been filled up
            if n == min(state):
                return 0

            state = list(state)
            # find the min height in state array
            mn = min(state)
            start = state.index(mn)
            res = INF

            # try to fill the lowest height with different size square, as long as the height doesn't exceed n after adding the square
            for end in range(start, m):
                if state[end] != mn:
                    break
                side = end - start + 1
                if mn + side > n:
                    break
                state[start:end+1] = [mn+side]*side
                res = min(res, 1 + dp(tuple(state)))

            return res

        return dp(tuple([0]*m))