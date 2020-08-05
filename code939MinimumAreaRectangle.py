"""
939 Minimum Area Rectangle

Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""
from collections import defaultdict
class Solution:
    # help from https://leetcode.com/problems/minimum-area-rectangle/solution/
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        columns = defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        
        lastx = {} # trick is to save the previous (y1, y2)
        ans = float('inf')
        for x in sorted(columns):
            column = sorted(columns[x]) # must sort each column too
            for i, y1 in enumerate(column):
                for j in range(i):
                    y2 = column[j]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[(y1, y2)])*(y1-y2))
                    lastx[(y1, y2)] = x
        
        #print(ans)
        return 0 if ans == float('inf') else ans

#points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
#points = [[1,1]]
points = [[3,2],[0,0],[3,3],[3,4],[4,4],[2,1],[4,3],[1,0],[4,1],[0,2]]
print(Solution().minAreaRect(points))