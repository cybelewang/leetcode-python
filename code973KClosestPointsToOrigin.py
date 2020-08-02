"""
973 K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 
Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""
from heapq import heappop, heappush
class Solution:
    # time O(NlogK), space O(K)
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        h = []
        for i, (x, y) in enumerate(points):
            heappush(h, (-x*x - y*y, i))
            if len(h) > K:
                heappop(h)
        
        res = []
        for _, i in h:
            res.append(points[i])
        
        return res

    # use quick sort's partition method to get partially sorted result
    # average time O(N), worset O(N^2), space O(K) for result list
    def kClosest2(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2
        def partition(s, e):
            # partition array to two parts, separated by pivot
            pivot = dist(e)
            i = s
            for j in range(s, e):
                if dist(j) < pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[e] = points[e], points[i]
            return i
        
        n = len(points)
        left, right = 0, n - 1
        while left <= right:
            i = partition(left, right)
            if i+1 == K: return points[:i+1] # bug fixed: i < n, but K could be n, so we must include [i] in the final result
            elif i < K:
                left = i + 1
            else:
                right = i - 1        

points = [[3,3],[5,-1],[-2,4]]
K = 2
print(Solution().kClosest(points, K))
print(Solution().kClosest2(points, K))