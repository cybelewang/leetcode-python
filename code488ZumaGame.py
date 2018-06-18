"""
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
from collections import Counter
class Solution:
    # http://www.cnblogs.com/grandyang/p/6759881.html
    # use brutal force dfs (implied by the size limit of board and hand), and help functions
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        def dfs(board, hand_count):
            if board == '':
                return 0

            ball_count = self.encode(board)
            steps = 100 # normally will not exceed 40 
            for index, [ball, count] in enumerate(ball_count):
                required = 3 - count
                if ball in hand_count and hand_count[ball] >= required:
                    ball_count[index][1] += required    # to become 3
                    hand_count[ball] -= required    # remove required number of balls from hand
                    next_board = self.remove_consecutive(self.decode(ball_count))   # remove 3 consecutive balls

                    steps = min(steps, required + dfs(next_board, hand_count))  # if any recursive call returns 100, the final result will be 100

                    # recover the balls to the condition before recursive call
                    hand_count[ball] += required
                    ball_count[index][1] -= required
            
            return steps

        hand_count = Counter(hand)
        steps = dfs(board, hand_count)
        if steps == 100:
            return -1
        else:
            return steps
                    
    def encode(self, s):
        """
        Encode string like 'RBYYBBRRB' to count R1B1Y2B2R2B1
        """
        prev, count, list_ = 'N', 0, []
        for c in s:
            if c == prev:
                count += 1
            else:
                if count > 0:
                    list_.append([prev, count])
                prev = c
                count = 1

        if count > 0:
            list_.append([prev, count])
        
        return list_

    def decode(self, ball_count):
        """
        Decode count R1B1Y2B2R2B1 to 'RBYYBBRRB'
        """
        s = ''
        for ball, count in ball_count:
            for _ in range(count):
                s += ball
        
        return s

    def remove_consecutive(self, balls):
        """
        remove three or more consecutive balls
        balls: input str
        return: str
        """
        res = []
        count, prev = 0, 'N'
        for b in balls:
            # res.append(b) # bug fixed: we should not put res.append(b) here!
            if prev == b:
                count += 1
            else:
                if count > 2:
                    for _ in range(count):
                        res.pop()
                count = 1
                prev = b
            res.append(b)
        
        if count > 2:
            for _ in range(count):
                res.pop()

        if len(res) == len(balls):
            return ''.join(res)
        else:
            return self.remove_consecutive(''.join(res))

obj = Solution()
print(obj.findMinStep("WRRBBW", "RB"))
