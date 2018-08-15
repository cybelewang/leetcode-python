"""
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. 
And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. 
If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:
Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
Example 2:
Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
Example 3:
Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
Hint: size of the given matrix will not exceed 50x50.
"""
# similar problems: 490 The Maze; 505 The Maze II
from collections import deque
class Solution:
    # maze (BFS) method to get min steps from A to B with obstacles
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        m, n = len(forest), len(forest[0])
        # push tuple (heigh, i, j) into a list
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        # sort the list based on the height (unique)
        trees.sort()

        row, col = 0, 0
        steps = 0
        for h, i, j in trees:
            cnt = self.bfs(forest, row, col, i, j)
            if cnt == -1:
                return -1
            else:
                steps += cnt
                row, col = i, j
        
        return steps

    def bfs(self, forest, row, col, tree_row, tree_col):
        """
        row, col: current position
        tree_row, tree_col: target tree position
        return min steps from current position to target tree position
        """
        if (row, col) == (tree_row, tree_col):
            return 0

        m, n = len(forest), len(forest[0])
        steps = 0
        visited = [[False]*n for _ in range(m)]
        dirs = ((0,-1), (-1, 0), (0, 1), (1, 0))
        q = deque()
        q.append((row, col))
        visited[row][col] = True
        while q:
            steps += 1
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if -1 < i < m and -1 < j < n and not visited[i][j] and forest[i][j] != 0:
                        if (i, j) == (tree_row, tree_col):
                            return steps
                        q.append((i, j))
                        visited[i][j] = True
                
        return -1

forest = [ [1,2,3], [0,0,4], [7,6,5] ]
print(Solution().cutOffTree(forest))