"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
# Ask if Interval's start <= end

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self): # __str__ for printing single object
        return '[' + str(self.start) + ', '+str(self.end) + ']'
    
    def __repr__(self): # __repr__ for printing this object in a iterable container
        return self.__str__()

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals or len(intervals) < 2:
            return intervals
        
        intervals.sort(key = lambda x: x.start)
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1].end < intervals[i].start:
                res.append(intervals[i])
            elif intervals[i].end > res[-1].end:
                res[-1].end = intervals[i].end
        
        return res

obj = Solution()
test_cases = [[], [[1, 2], [1, 3]], [[1, 10],[1,2]], [[1,3],[2,6],[8,10],[15,18]]]
for case in test_cases:
    print(case, end = ' -> ')
    intervals = []
    for element in case:
        intervals.append(Interval(element[0],element[1]))
    print(obj.merge(intervals))