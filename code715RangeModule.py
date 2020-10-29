"""
715 Range Module

A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.

addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is currently being tracked.
removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).
Example 1:
addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true (Every number in [10, 14) is being tracked)
queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
Note:

A half open interval [left, right) denotes all real numbers left <= x < right.
0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
The total number of calls to addRange in a single test case is at most 1000.
The total number of calls to queryRange in a single test case is at most 5000.
The total number of calls to removeRange in a single test case is at most 1000.
"""
# better to use Java's TreeSet
from bisect import bisect_left
# find out the affected bounds and update the bounds
# the _bounds() method helps to find out the bounds
class RangeModule:

    def __init__(self):
        self.data = [] 

    # find the index range in self.data that self.data[i:j] are affected by the given [left, right)
    def _bounds(self, left, right):
        # find the first index that its start >= left, but i-1's end may >= left
        i = bisect_left(self.data, (left, left))
        # check if i-1's end >= left, if so, decrease i by 1 
        if i > 0 and self.data[i-1][1] >= left:
            i -= 1
        # find the first index that its start > right, this includes the interval that has start == right
        # we need to set the find interval's end to INT_MAX to include intervals that has start == right
        j = bisect_left(self.data, (right, 2**31-1))
        return (i, j)

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        i, j = self._bounds(left, right)
        if i < j:
            left = min(left, self.data[i][0])
            right = max(right, self.data[j-1][1])
        self.data[i:j] = [(left, right)]      

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        i = bisect_left(self.data, (left, 2**31-1))
        return i > 0 and self.data[i-1][0] <= left and self.data[i-1][1] >= right       

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        i, j = self._bounds(left, right)
        merge = []
        for k in range(i, j):
            if self.data[k][0] < left:
                merge.append((self.data[k][0], left))
            if self.data[k][1] > right:
                merge.append((right, self.data[k][1]))
        self.data[i:j] = merge
        
# traditional add/remove methods, have bugs
from bisect import bisect
class RangeModule2:

    def __init__(self):
        self.data = []        

    def addRange(self, left: int, right: int) -> None:
        i = bisect(self.data, [left, 2**31-1])
        if i > 0 and self.data[i-1][1] > left:
            self.data[i-1][1] = max(self.data[i-1][1], right)
            i -= 1
        else:
            self.data.insert(i, [left, right])
            
        while i + 1 < len(self.data) and self.data[i][1] >= self.data[i+1][0]:
            self.data[i][1] = max(self.data[i][1], self.data[i+1][1])
            self.data.pop(i+1) 
        #print(self.data)

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect(self.data, [left, 2**31-1])
        if (left, right) == (9, 56):
            print(self.data)
        return i > 0 and self.data[i-1][0] <= left and self.data[i-1][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        i = bisect(self.data, [left, 2**31-1])
        if i > 0:
            if self.data[i-1][1] > right:
                temp = self.data[i-1][1]
                self.data[i-1][1] = left
                self.data.insert(i, [right, temp])          
            elif self.data[i-1][1] > left:
                self.data[i-1][1] = left
            
        while i < len(self.data) and self.data[i][1] < right:
            self.data.pop(i)  
        
        if i < len(self.data):
            self.data[i][0] = max(self.data[i][0], right)
        #print(self.data)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)