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
from heapq import heappush, heappop
class Solution:
    # MinHeap + BFS
    # 1. push all board cells into MinHeap by comparing the height, and mark them as "visited"
    # 2. poll the first (min) cell from MinHeap, and check its non-visited neighbors, if neighbor's height < this cell's height, add difference into res, 
    # and push the neighbor cell (with >= this cell's height) into MinHeap, mark this neighbor as visited
    # we always process the minimum height cell first, because it determines the plank level
    # https://leetcode.com/problems/trapping-rain-water-ii/discuss/89461/Java-solution-using-PriorityQueue
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False]*n for _ in range(m)]
        neighbors = [(0, -1), (-1, 0), (0, 1), (1, 0)] # left, above, right, below
        queue = []

        # push top and bottom row cells into MinHeap
        for row in {0, m-1}:# use a set to avoid adding the first row into MinHeap twice
            for j in range(n):
                heappush(queue, (heightMap[row][j], row, j))
                visited[row][j] = True
        
        for col in {0, n-1}:
            for i in range(1, m-1):
                heappush(queue, (heightMap[i][col], i, col))
                visited[i][col] = True
        
        res = 0
        # BFS from outer to inner, like peeling the onion
        while queue:
            height, row, col = heappop(queue)
            for dx, dy in neighbors:
                i, j = row + dx, col + dy
                if -1 < i < m and -1 < j < n and not visited[i][j]:
                    visited[i][j] = True
                    res += max(0, height - heightMap[i][j]) # avoid using if-else
                    heappush(queue, (max(height, heightMap[i][j]), i, j))   # tricky!!!
        
        return res

    # Below is a wrong solution. The reason is that the plank water level may not be determined by that column or row, see [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
    # similar to 42, trapping raing water
    # here we use a mxn matrix to store the trapped water
    # first fill matrix row by row, using the method in problem 42
    # then fill matrix column by column, and take the minimum value
    # finally sum all water in the matrix
    def trapRainWater2(self, heightMap):
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
        print(water)    
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

        print(water)
        # 2d sum, see https://stackoverflow.com/questions/33541947/what-does-the-built-in-function-sum-do-with-sumlist
        return sum(sum(water, []))

heightMap = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
obj = Solution()
print(obj.trapRainWater(heightMap))
"""
12	13	1	12
13	4	13	12
13	8	10	12
12	13	12	12
13	13	13	13
"""

"""
public class Solution {

    public class Cell {
        int row;
        int col;
        int height;
        public Cell(int row, int col, int height) {
            this.row = row;
            this.col = col;
            this.height = height;
        }
    }

    public int trapRainWater(int[][] heights) {
        if (heights == null || heights.length == 0 || heights[0].length == 0)
            return 0;

        PriorityQueue<Cell> queue = new PriorityQueue<>(1, new Comparator<Cell>(){
            public int compare(Cell a, Cell b) {
                return a.height - b.height;
            }
        });
        
        int m = heights.length;
        int n = heights[0].length;
        boolean[][] visited = new boolean[m][n];

        // Initially, add all the Cells which are on borders to the queue.
        for (int i = 0; i < m; i++) {
            visited[i][0] = true;
            visited[i][n - 1] = true;
            queue.offer(new Cell(i, 0, heights[i][0]));
            queue.offer(new Cell(i, n - 1, heights[i][n - 1]));
        }

        for (int i = 0; i < n; i++) {
            visited[0][i] = true;
            visited[m - 1][i] = true;
            queue.offer(new Cell(0, i, heights[0][i]));
            queue.offer(new Cell(m - 1, i, heights[m - 1][i]));
        }

        // from the borders, pick the shortest cell visited and check its neighbors:
        // if the neighbor is shorter, collect the water it can trap and update its height as its height plus the water trapped
       // add all its neighbors to the queue.
        int[][] dirs = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int res = 0;
        while (!queue.isEmpty()) {
            Cell cell = queue.poll();
            for (int[] dir : dirs) {
                int row = cell.row + dir[0];
                int col = cell.col + dir[1];
                if (row >= 0 && row < m && col >= 0 && col < n && !visited[row][col]) {
                    visited[row][col] = true;
                    res += Math.max(0, cell.height - heights[row][col]);
                    queue.offer(new Cell(row, col, Math.max(heights[row][col], cell.height)));
                }
            }
        }
        
        return res;
    }
}
"""