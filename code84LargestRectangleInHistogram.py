"""
84 Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        hist = []

        i = 0
        while i < len(heights):
            if not hist or heights[hist[-1]] <= heights[i]:
                hist.append(i)
                i += 1
            else:
                h = heights[hist.pop()]
                if not hist:
                    w = i
                else:
                    w = i - 1 - hist[-1]
                maxArea = max(h*w, maxArea)
        
        while hist:
            h = heights[hist.pop()]
            if not hist:
                w = len(heights)
            else:
                w = len(heights) - 1 - hist[-1]
            maxArea = max(h*w, maxArea)
        
        return maxArea

test_case = [1,0, 1,0,1]
obj = Solution()
print(obj.largestRectangleArea(test_case))