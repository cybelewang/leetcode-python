"""
305 Number of Islands II

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example:
Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:
Can you do it in time complexity O(k log mn), where k is the length of the positions?
"""
import unittest
class Solution:
    def numIslands2(self, m, n, positions):
        def find(root, i):
            while i != root[i]:
                i = root[i]
            return i
        
        root = [-1]*(m*n)   # initial value -1 means water
        dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        cnt, res = 0, []
        for x, y in positions:
            id = x*n + y # encode the position
            if root[id] == -1: # bug fixed: don't forget to check if this position is on water, we may still put island on island
                cnt += 1
                root[id] = id # make this position a new group
            p = find(root, id)
            for dx, dy in dirs: # iterate neighboring cells and try to union to an existing group
                i, j = x + dx, y + dy
                if -1 < i < m and -1 < j < n:
                    cur_id = i * n + j
                    if root[cur_id] == -1: continue # this neighbor is water, skip
                    q = find(root, cur_id)
                    if p != q:  # only union neighors if the root value is different
                        root[p] = q
                        cnt -= 1 # only count 1 when union different groups, imagine the case when a cell connects two ends of a group. When connecting the left end, we count 1, and when connecting the right end, we don't count because they have the same root.
            res.append(cnt)

        return res

class Test(unittest.TestCase):
    def test_1(self):
        obj = Solution()
        positions = [[1,1],[2,0],[2,2],[3,1], [2, 1]]
        self.assertEqual(obj.numIslands2(4, 4, positions), [1, 2, 3, 4, 1])
    def test_2(self):
        obj = Solution()
        positions = [[0,0],[0,1],[1,2],[1,2]]
        self.assertEqual(obj.numIslands2(3, 3, positions), [1, 1, 2, 2])

if __name__ == "__main__":
    unittest.main(exit=False)