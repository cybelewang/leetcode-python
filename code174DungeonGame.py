"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	   3
-5	    -10	   1
10	    30	   -5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""
class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        M, N = len(dungeon), len(dungeon[0])
        dungeon[M-1][N-1] = 1 - dungeon[M-1][N-1] if dungeon[M-1][N-1] < 1 else 1

        for i in range(M-2, -1, -1):
            dungeon[i][N-1] = dungeon[i+1][N-1] - dungeon[i][N-1] if dungeon[i+1][N-1] > dungeon[i][N-1] else 1
        
        for j in range(N-2, -1, -1):
            dungeon[M-1][j] = dungeon[M-1][j+1] - dungeon[M-1][j] if dungeon[M-1][j+1] > dungeon[M-1][j] else 1
        
        for i in range(M-2, -1, -1):
            for j in range(N-2, -1, -1):
                minHP = min(dungeon[i+1][j], dungeon[i][j+1])
                dungeon[i][j] = minHP - dungeon[i][j] if minHP > dungeon[i][j] else 1

        return dungeon[0][0]
    
    # first try, from top left to right bottom, has bug
    def calculateMinimumHP2(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        def getRemainHP(prevRemain, prevMinHP, curHP):
            if prevRemain + curHP > 0:
                return (prevRemain + curHP, prevMinHP)
            else:
                return (1, 1 - prevRemain - curHP + prevMinHP)


        M, N = len(dungeon), len(dungeon[0])
        minHP = [[1 for j in range(N)] for i in range(M)]   # dp matrix for minimum HP
        dungeon[0][0], minHP[0][0] = getRemainHP(1, 1, dungeon[0][0])

        for i in range(1, M):
            dungeon[i][0], minHP[i][0] = getRemainHP(dungeon[i-1][0], minHP[i-1][0], dungeon[i][0])
        
        for j in range(1, N):
            dungeon[0][j], minHP[0][j] = getRemainHP(dungeon[0][j-1], minHP[0][j-1], dungeon[0][j])

        for i in range(1, M):
            for j in range(1, N):
                topRemHP, topMinHP = getRemainHP(dungeon[i-1][j], minHP[i-1][j], dungeon[i][j])
                leftRemHP, leftMinHP = getRemainHP(dungeon[i][j-1], minHP[i][j-1], dungeon[i][j])
                if topMinHP < leftMinHP:    # wrong here. What about topRemHP > leftRemHP when topMinHP < leftMinHP?
                    dungeon[i][j], minHP[i][j] = topRemHP, topMinHP
                elif topMinHP > leftMinHP:  # wrong here, what about leftRemHp > topRemHP when topMinHP > leftMinHP?
                    dungeon[i][j], minHP[i][j] = leftRemHP, leftMinHP
                else:
                    dungeon[i][j] = max(topRemHP, leftRemHP)
                    minHP[i][j] = leftMinHP
        
        return minHP[M-1][N-1]

obj = Solution()
test_case = [[-3, 0, 3]]#[[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
print(obj.calculateMinimumHP(test_case))
