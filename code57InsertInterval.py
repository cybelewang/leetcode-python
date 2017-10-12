"""
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
        if not intervals:
            return newInterval
        elif not newInterval:
            return intervals
        
        # Binary search for the insertion position
        s, e = 0, len(intervals) - 1
        while s <= e:
            mid = (s + e)//2
            if newInterval.start == intervals[mid].start:
                 

