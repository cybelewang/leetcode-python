"""
963 Minimum Area Rectangle II

Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.

If there isn't any rectangle, return 0.

Example 1:

Input: [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
Example 2:

Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
Example 3:

Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.
Example 4:

Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.

Note:

1 <= points.length <= 50
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
Answers within 10^-5 of the actual value will be accepted as correct.
"""
import collections
import itertools
class Solution:
    # https://leetcode.com/articles/minimum-area-rectangle-ii/
    # O(N^2 * logN)
    # consider every two-point pair, and calculate their center and radius
    # if two pairs share the same center and radius, they must be able to form a rectangle
    def minAreaFreeRect(self, points):
        """
        :type Points: list[list[int]]
        :rtype: float
        """
        points = [complex(*z) for z in points]
        seen = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q)/2
            radius = abs(center - P)
            seen[(center, radius)].append(P)
        
        ans = float('inf')
        for (center, radius), candidates in seen.items():
            for P, Q in itertools.combinations(candidates, 2):
                ans = min(ans, abs(P-Q) * abs(P-(2*center - Q)))
        
        return ans if ans < float('inf') else 0
    
    # https://leetcode.com/articles/minimum-area-rectangle-ii/
    # O(N^3 * logN)
    def minAreaFreeRect2(self, points):
        EPS = 1e-7
        points = set(map(tuple, points))

        ans = float('inf')
        for p1, p2, p3 in itertools.permutations(points, 3):
            p4 = p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1]
            if p4 in points:
                v21 = complex(p2[0] - p1[0], p2[1] - p1[1])
                v31 = complex(p3[0] - p1[0], p3[1] - p1[1])
                if abs(v21.real*v31.real + v21.imag*v31.imag) < EPS:    #check if p1-p2 and p1-p3 are orthognal
                    area = abs(v21)*abs(v31)
                    if area < ans:
                        ans = area
        
        return ans if ans < float('inf') else 0

points = [[1,2],[2,1],[1,0],[0,1]]
print(Solution().minAreaFreeRect2(points))