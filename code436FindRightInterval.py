"""
436 Find Right Interval


Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. 
If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
Example 1:
Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:
Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
Example 3:
Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
"""
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

from bisect import bisect_left, insort_left
class Solution:
    # OJ's best
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        minVal = 100000
        maxVal = -100000
        for interval in intervals:
            minVal = min(minVal, interval.start)
            maxVal = max(maxVal, interval.end)
        
        bucketLength = maxVal -minVal + 1
        bucket = [-1] * bucketLength
        for index, interval in enumerate(intervals):
            bucket[interval.start - minVal] = index
        
        for i in range(len(bucket) - 2, -1, -1):
            if bucket[i] == -1:
                bucket[i] = bucket[i + 1]
        
        result = [-1] * len(intervals)
        for index, interval in enumerate(intervals):
            result[index] = bucket[interval.end - minVal]
        return result
    # My solution
    # Add tuple(start, index) into a binary search array using the bisect_left method, O(n)
    # For each interval, find the insertion index for interval.end in the above tuple array, and append the index in tuple, O(logn)
    # The overall time complexity is O(nlogn)
    def findRightInterval2(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        starts = []
        for (i, interval) in enumerate(intervals):
            insort_left(starts, (interval.start, i))

        res = []
        for interval in intervals:
            index = bisect_left(starts, (interval.end, 0))
            if index == len(starts):
                res.append(-1)
            else:
                res.append(starts[index][1])

        return res

input = [ [1,2] ]
intervals = [Interval(s, e) for (s, e) in input]

obj = Solution()
print(obj.findRightInterval(intervals))