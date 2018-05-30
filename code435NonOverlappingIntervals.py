"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
Example 1:
Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:
Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:
Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""
# similar to problem 452, Minimum Number of Arrows to Burst Balloons
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # sort the intervals based on their start value
    # then iterate all the intervals, when seeing overlapped intervals, always keep the interval with smaller end value
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        intervals.sort(key = lambda x : x.start)
        ref, res = intervals[0], 0
        for i in range(1, len(intervals)):
            if intervals[i].start < ref.end:
                res += 1
                if intervals[i].end >= ref.end:
                    continue
            ref = intervals[i]

        return res

#input = [[1,4],[2,3],[3,4]]
#input = [ [1,2], [2,3], [3,4], [1,3] ]
input = [ [1,2], [1,2], [1,2] ]
intervals = [Interval(s, e) for (s, e) in input]

obj = Solution()
print(obj.eraseOverlapIntervals(intervals))
