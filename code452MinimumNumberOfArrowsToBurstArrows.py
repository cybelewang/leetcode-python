"""
452 Minimum Number of Arrows to Burst Balloons

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 10^4 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""
# similar to 354 Russian Doll Envelopes, 435 Non-overlapping intervals
# first sort all balloons based on the end, then iterate the ballons, for each balloon, try to shoot its end position, and then remove corresponding balloons
class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x:x[1])
        i, shots = 0, 0
        while i < len(points):
            shots += 1
            j = i + 1
            while j < len(points) and points[j][0] <= points[i][1]:
                j += 1
                
            i = j
        
        return shots

    # 2nd round solution on 6/3/2019
    def findMinArrowShots2(self, points):
        if not points:
            return 0
        # sort points based on end positions
        points.sort(key = lambda x: x[1])
        end, res = points[0][1], 1
        for i in range(1, len(points)):
            if points[i][0] > end:
                end = points[i][1]
                res += 1
        
        return res

    # 3rd round solution on 6/3/2019, easier to understand
    def findMinArrowShots3(self, points):
        if not points:
            return 0
        points.sort()
        s, e = points[0]    # s and e are the current arrow's shoot range
        res = 1
        for i in range(1, len(points)):
            if points[i][0] <= e:
                # save an arrow
                s = max(s, points[i][0])
                e = min(e, points[i][1])
            else:
                s, e = points[i]
                res += 1
        
        return res

    # from above solution we can see "s" is unused, so we just use single variable to track arrow's end
    # also see https://www.cnblogs.com/grandyang/p/6050562.html
    def findMinArrowShots4(self, points):
        if not points:
            return 0
        points.sort()
        end, res = points[0][1], 1
        for i in range(1, len(points)):
            if points[i][0] <= end:
                end = min(end, points[i][1])
            else:
                res += 1
                end = points[i][1]
        
        return res

points = [[10,16], [2,8], [1,6], [7,12]]
obj = Solution()
print(obj.findMinArrowShots3(points))