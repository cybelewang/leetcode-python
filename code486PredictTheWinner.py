"""
486 Predict the Winner

Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. 
Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.
Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
"""
# similar problems: 375, 464
from collections import deque
class Solution:
    # http://www.cnblogs.com/grandyang/p/6369688.html
    # DP, The dp[i][j] saves how much more scores that the current active player will get from i to j than the other player. 
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3: return True
        dp = [[-1]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            dp[i][i] = nums[i]
            for j in range(i+1, n):
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        
        # for i in range(n):
        #     dp[i][i] = nums[i]
        
        # for right in range(1, n):
        #     i, j = 0, right
        #     while j < n:
        #         dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        #         i += 1
        #         j += 1
        
        return dp[0][n-1] >= 0

    # recursive + DP
    # easier to understand
    def PredictTheWinner2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def CanWin(nums, i, j, dp):
            if dp[i][j] == -1:
                dp[i][j] = nums[i] if i == j else max(nums[i] - CanWin(nums, i + 1, j, dp), nums[j] - CanWin(nums, i, j - 1, dp))
            
            return dp[i][j]
        
        n = len(nums)
        if n < 3: return True
        dp = [[-1]*n for _ in range(n)]

        return CanWin(nums, 0, n-1, dp) >= 0

    # recursive solution, easier to understand
    def PredictTheWinner3(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # why this is the wrong recursive function? [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], should be true
        def CanWin(nums, i, j, score1, score2, player):
            if i == j:
                if player == 1:
                    return score1 + nums[i] >= score2
                else:
                    return score2 + nums[i] > score1    # bug fixed: cannot use >=, should be > because the description says "equal" also means player 1 wins
            else:
                if player == 1:
                    return (not CanWin(nums, i+1, j, score1 + nums[i], score2, 2)) or (not CanWin(nums, i, j-1, score1 + nums[j], score2, 2))
                else:
                    return (not CanWin(nums, i+1, j, score1, score2 + nums[i], 1)) or (not CanWin(nums, i, j-1, score1, score2 + nums[j], 1))

        # this is a wrong recursive function, consider case [2,4,55,6,8], should be false
        def CanWin_Wrong(nums, i, j, score1, score2, player):
            if i == j:  # just one number left
                if player == 1:
                    score1 += nums[i]
                else:
                    score2 += nums[i]

                return score1 >= score2
            elif j - i == 1:    # two numbers left
                if player == 1:
                    score1 += max(nums)
                    score2 += min(nums)
                else:
                    score1 += min(nums)
                    score2 += max(nums)

                return score1 >= score2
            else:   # three or more numbers, need recursive calls
                if player == 1:
                    return CanWin_Wrong(nums, i + 1, j, score1 + nums[i], score2, 2) or CanWin_Wrong(nums, i, j-1, score1 + nums[j], score2, 2)
                else:
                    return CanWin_Wrong(nums, i+1, j, score1, score2 + nums[i], 1) or CanWin_Wrong(nums, i, j-1, score1, score2 + nums[j], 1)

        if len(nums) < 3:
            return True
        else:
            return CanWin(nums, 0, len(nums)-1, 0, 0, 1)

    # 2nd round recursive solution on 4/30/2019
    # TLE
    def PredictTheWinner4(self, nums):
        def canWin(q, scores, player):
            """
            q: deque of remaining numbers
            scores: [player 1's score, player 2's score]
            player: 0 represents player 1, 1 represents player 2            
            """
            if len(q) == 0: # this handles the case when input nums is empty
                return scores[0] >= scores[1]
            elif len(q) == 1:   # this is the normal convergence condition
                if player == 0:
                    return scores[0] + q[0] >= scores[1]
                else:
                    return scores[1] + q[0] > scores[0]
            
            # pick up the front number
            cur = q.popleft()
            scores[player] += cur
            res1 = not canWin(q, scores, player^1)
            # restore the front number
            scores[player] -= cur
            q.appendleft(cur)

            # pick up the back number
            cur = q.pop()
            scores[player] += cur
            res2 = not canWin(q, scores, player^1)
            # restore the back number
            scores[player] -= cur
            q.append(cur)

            return res1 or res2

        # main
        q = deque(nums)
        return canWin(q, [0, 0], 0)    

#nums = [1, 5, 2]    # expect false
#nums = [1, 5, 7, 6] # expect true
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]    # expect true
print(Solution().PredictTheWinner(nums))