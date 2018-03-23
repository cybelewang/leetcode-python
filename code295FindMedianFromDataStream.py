"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
"""
# ORDERED interger list!!!
# use max heap and min heap to get the median
# large heap | small heap
# heapq module is a min heap, to get max heap, manually add a negative sign
from heapq import *
class MedianFinder:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []  # get max from left half
        self.right = [] # get min from right half

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heappush(self.left, -heappushpop(self.right, num))
        if len(self.left) > len(self.right):
            heappush(self.right, -heappop(self.left))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.right) > len(self.left):
            return self.right[0]*1.0
        else:
            return (self.right[0] - self.left[0])/2.0

obj = MedianFinder()
obj.addNum(6)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())
obj.addNum(8)
print(obj.findMedian())

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()