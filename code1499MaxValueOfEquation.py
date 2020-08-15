"""
1499 Max Value of Equation

Given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length. It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

Example 1:

Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.
Example 2:

Input: points = [[0,0],[3,0],[9,2]], k = 3
Output: 3
Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.

Constraints:

2 <= points.length <= 10^5
points[i].length == 2
-10^8 <= points[i][0], points[i][1] <= 10^8
0 <= k <= 2 * 10^8
points[i][0] < points[j][0] for all 1 <= i < j <= points.length
xi form a strictly increasing sequence.
"""

from collections import deque
class Solution:
    # equation is (yi - xi) + yj + xj, so for each point j, we need to find i with largest yi-xi, and xj-xi<=k
    # mono-decrease-deque solution, maintaining y-x in descending order
    def findMaxValueOfEquation(self, points, k):
        q, res = deque(), -2**31
        for x, y in range(len(points)):
            # remove points that has x differ > k
            while q and points[q[0]][0] + k < x: 
                q.popleft()
            # update result using q's front element, which has the largest yi-xi
            if q: res = max(res, y + points[q[0]][1] + x - points[q[0]][0])
            # remove elements with smaller yi-xi
            while q and y - x >= points[q[-1]][1] - points[q[-1]][0]:
                q.pop()

            q.append(j)
       
        return res

    # my own solution using mono-decreasing deque, large on left, small on right
    # for each new point, we pop left all points that have x diff > k, and update result in popping process
    # then we pop right all points that <= current point's y, and update result in popping process. A bug here because y should not be the mono-deque's maintaince logic, it should be y-x
    # see example points = [[-19,-12],[-5,-18],[2,-2],[10,3],[11,-3],[13,17]], k = 13, we will find [2, -2] will be popped by [10, 3], but actually later [13, 17] will form a larger value.
    # lastly, we calculate and update equation for elements remaining in deque
    def findMaxValueOfEquation_BUG(self, points, k):
        def cal(points, i, j):
            return points[i][1] + points[j][1] + points[j][0] - points[i][0]

        q, res = deque(), -2**31
        for j in range(len(points)):
            while q and points[q[0]][0] + k < points[j][0]:
                i = q.popleft()
                for e in q:
                    res = max(res, cal(points, i, e))
            last_pop = -1
            while q and points[j][1] >= points[q[-1]][1]:
                last_pop = q.pop()
            if not q and last_pop != -1:
                res = max(res, cal(points, last_pop, j))
            q.append(j)
            
        while q:
            i = q.popleft()
            for e in q:
                res = max(res, cal(points, i, e))
        
        return res

#points = [[-19,-12],[-13,-18],[-12,18],[-11,-8],[-8,2],[-7,12],[-5,16],[-3,9],[1,-7],[5,-4],[6,-20],[10,4],[16,4],[19,-9],[20,19]]
#k = 6
points = [[-19,-12],[-5,-18],[2,-2],[10,3],[11,-3],[13,17]]
k = 13 # expect 26
print(Solution().findMaxValueOfEquation(points, k))