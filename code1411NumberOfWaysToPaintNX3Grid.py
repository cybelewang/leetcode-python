"""
1411 Number of Ways to Paint N × 3 Grid

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

Example 1:

Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown:

Example 2:

Input: n = 2
Output: 54
Example 3:

Input: n = 3
Output: 246
Example 4:

Input: n = 7
Output: 106494
Example 5:

Input: n = 5000
Output: 30228214

Constraints:
n == grid.length
grid[i].length == 3
1 <= n <= 5000
"""
# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/discuss/574923/JavaC%2B%2BPython-DP-O(1)-Space
# Group every row to "121" style and "123" style, here "121" means first and third color are the same, "123" means all three colors are different
# For "121", it can be followed by "212", "213", "232", "312", "313"
# For "123", it can be followed by "212", "231", "232", "312"
class Solution:
    def numOfWays(self, n: int) -> int:
        a121, a123 = 6, 6
        M = 10**9 + 7
        for _ in range(n-1):
            b121, b123 = a121*3 + a123*2, a121*2 + a123*2
            a121, a123 = b121 % M, b123 % M
        
        return (a121 + a123) % M