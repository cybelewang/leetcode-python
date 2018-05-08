"""

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.


After the rain, water is trapped between the blocks. The total volume of water trapped is 4.
"""
# similar to 42, trapping raing water
# here we use a mxn matrix to store the trapped water
# first fill matrix row by row, using the method in problem 42
# then fill matrix column by column, and take the minimum value
# finally sum all water in the matrix
class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        water = [[0]*n for _ in range(m)]
        plank = 0
        
        # get trapped water row by row
        for i in range(m):
            plank, l, r = 0, 0, n-1
            while l <= r:
                plank = max(plank, min(heightMap[i][l], heightMap[i][r]))
                if heightMap[i][l] <= heightMap[i][r]:
                    water[i][l] = plank - heightMap[i][l]
                    l += 1
                else:
                    water[i][r] = plank - heightMap[i][r]
                    r -= 1
            
        # get trapped water column by column
        for j in range(n):
            plank, l, r = 0, 0, m-1
            while l <= r:
                plank = max(plank, min(heightMap[l][j], heightMap[r][j]))
                if heightMap[l][j] <= heightMap[r][j]:
                    water[l][j] = min(water[l][j], plank - heightMap[l][j])
                    l += 1
                else:
                    water[r][j] = min(water[r][j], plank - heightMap[r][j])
                    r -= 1
        # 2d sum, see https://stackoverflow.com/questions/33541947/what-does-the-built-in-function-sum-do-with-sumlist
        return sum(sum(water, []))

heightMap = [[1,4,3,1,3,2], [3,2,1,3,2,4], [2,3,3,2,3,1]]
obj = Solution()
print(obj.trapRainWater(heightMap))