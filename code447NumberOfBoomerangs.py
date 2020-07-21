"""
447 Number of Boomerangs

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""
from collections import defaultdict
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        count = defaultdict(int)
        res = 0
        for i in range(n):
            count.clear()
            for j in range(n):
                if i == j:
                    continue
                else:
                    d2 = (points[j][1] - points[i][1])**2 + (points[j][0]-points[i][0])**2
                    res += 2*count[d2] # count[d2] means [points[i], previous points with d2 from points[i], points[j]], another count[d2] is [points[i], points[j], previous points with d2 from points[i]]
                    count[d2] += 1
        
        return res

input = [[0,0],[1,0],[2,0]]
obj = Solution()
print(obj.numberOfBoomerangs(input))