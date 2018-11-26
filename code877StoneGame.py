"""
877 Stone Game

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

Example 1:

Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
"""
# similar problems: 464 Can I Win
class Solution:
    # help from https://leetcode.com/problems/stone-game/solution/
    # change the game so that whenever Lee scores points, it deducts from Alex's score instead.
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        N = len(piles)

        dp = [[0]*(N+2) for _ in range(N+2)]    # dp[i+1][j+1] = the value of the game [piles[i], ..., piles[j]].
        for size in range(1, N+1):  # size from 1 to N
            for i in range(N-size+1):   # the upper including limit of i is (N - size), considering i + size == N
                j = i + size - 1    # j - i + 1 == size
                parity = (j + i + N) % 2    # 1 for Alex
                if parity == 1:
                    dp[i+1][j+1] = max(piles[i] + dp[i+2][j+1], piles[j] + dp[i+1][j])
                else:
                    dp[i+1][j+1] = min(-piles[i] + dp[i+2][j+1], -piles[j] + dp[i+1][j])
        
        return dp[1][N] > 0

piles = [5,3,4,5]
print(Solution().stoneGame(piles))