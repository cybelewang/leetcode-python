"""
57 Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self): # __str__ for printing single object
        return '[' + str(self.start) + ', '+str(self.end) + ']'
    
    def __repr__(self): # __repr__ for printing this object in a iterable container
        return self.__str__()

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals or len(intervals) < 1:
            return [newInterval]
        elif not newInterval:
            return intervals

        # Corner case 1: newInterval.end < intervals[0].start
        if newInterval.end < intervals[0].start:
            intervals.insert(0, newInterval)
            return intervals

        # Corner case 2: newInterval.start > intervals[-1].end
        if newInterval.start > intervals[-1].end:
            intervals.append(newInterval)
            return intervals
        
        res = []
        included = False
        for e in intervals:
            if e.end < newInterval.start: # e is smaller than newInterval
                res.append(e)
            else:
                if not included:
                    res.append(newInterval)
                    included = True
                
                if e.start > newInterval.end:
                    res.append(e)
                else:
                    newInterval.start = min(newInterval.start, e.start)
                    newInterval.end = max(newInterval.end, e.end)
                    
        return res

obj = Solution()
case = [[1,2],[5,6],[8,10]]
intervals = []
for element in case:
    intervals.append(Interval(element[0],element[1]))

print(obj.insert(intervals, Interval(2,6)))