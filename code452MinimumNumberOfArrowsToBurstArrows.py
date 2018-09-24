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

points = [[10,16], [2,8], [1,6], [7,12]]
obj = Solution()
print(obj.findMinArrowShots(points))