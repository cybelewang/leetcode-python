"""
1025 Divisor Game

Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

Example 1:
Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.

Example 2:
Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.

Note:

1 <= N <= 1000
"""
# tag: game theory
# similar problems: 464 Can I Win
from math import sqrt, floor
class Solution:
    # my own solution using DFS + cache
    def divisorGame_DFS(self, N):
        """
        :type N: int
        :rtype: bool
        """
        def win(number, cache):
            if number in cache:
                return cache[number]
            
            other_win = False
            for i in range(1, floor(sqrt(number)) + 1):
                if number % i == 0:
                    other_win = other_win or win(number - i, cache)
            
            this_win = not other_win
            cache[number] = this_win

            return this_win
        
        # main
        cache = {0:False, 1:False, 2:True}
        return win(N, cache)

N = 4
print(Solution().divisorGame_DFS(N))
