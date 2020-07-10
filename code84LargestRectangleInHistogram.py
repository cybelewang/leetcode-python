"""
84 Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""
import unittest
# similar problems: 42 Trapping Rain Water
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        hist = []   # a stack that holds indices with values in ascending order

        i = 0
        while i < len(heights):
            if not hist or heights[hist[-1]] <= heights[i]:
                hist.append(i)
                #print('append ' + str(heights[i]) + ' at '+ str(i))
                i += 1
            else:   # if last value in stack is greater than current one, pop it out and calculate the corresponding area
                #print('pop ' + str(heights[hist[-1]]) + ' at ' + str(hist[-1]), end = None)
                h = heights[hist.pop()]
                if not hist:
                    w = i
                else:
                    w = i - 1 - hist[-1]
                #print(', h = ' + str(h), ', w = ' + str(w), ', area = ' + str(h*w))
                maxArea = max(h*w, maxArea)
        
        while hist:
            h = heights[hist.pop()]
            if not hist:
                w = len(heights)
            else:
                w = len(heights) - 1 - hist[-1]
            maxArea = max(h*w, maxArea)
        
        return maxArea


    # 2nd visit on 9/20/2018, cannot work it out

    # 3rd visit on 7/9/2020, need help from onenote
    def largestRectangleArea2(self, heights):
        heights.append(0)   # trick to pop all elements from stack at the end of array
        stack, res = [], 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                minH = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                res = max(res, minH*width)
            stack.append(i)
        
        return res

class Test(unittest.TestCase):
    def test_1(self):
        obj = Solution()
        test_case = [2, 1, 5, 6, 2, 3]
        self.assertEqual(obj.largestRectangleArea2(test_case), 10)

    def test_2(self):
        obj = Solution()
        test_case = [1,0, 1,0,1]
        self.assertEqual(obj.largestRectangleArea2(test_case), 1)

if __name__ == "__main__":
    unittest.main(exit=False)