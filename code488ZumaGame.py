"""
488 Zuma Game

Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 

Note:
You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the input.
The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
"""
import itertools, collections
import unittest
class Solution:
    # http://www.cnblogs.com/grandyang/p/6759881.html
    # use brutal force dfs (implied by the size limit of board and hand), and help functions
    def findMinStep(self, board: str, hand: str) -> int:
        def removeConsecutiveBalls(s):
            # remove >= 3 continuous balls
            res = []
            for k, g in itertools.groupby(s):
                group = list(g)
                if len(group) < 3:
                    res.extend(group)
            if len(res) == len(s):
                return s
            else:
                return removeConsecutiveBalls(''.join(res))
        
        avails = collections.Counter(hand)
        
        def helper(board, avails):
            board = removeConsecutiveBalls(board)
            if not board: return 0
            path, start = 100, 0
            for i in range(0, len(board)+1):
                for ball in 'RYBGW':
                    if avails[ball] > 0:
                        next_board = board[:i] + ball + board[i:]
                        avails[ball] -= 1
                        path = min(path, 1 + helper(next_board, avails))
                        avails[ball] += 1
            return path
        
        ans = helper(board, avails)
        if ans == 100:
            return -1
        return ans

obj = Solution()
print(obj.findMinStep("RRWWRRBBRR", "WB")) # expect 2
# RRWWRRBBR[W]R
# RRWWRRBB[B]R[W]R
# RRWWRRRWR
# RRWWWR
# RRR
# ""