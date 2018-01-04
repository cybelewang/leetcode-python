"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
"""
from math import *
class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        
        # get min and max values
        minVal, maxVal = nums[0], nums[0]
        for num in nums:
            minVal = min(minVal, num)
            maxVal = max(maxVal, num)
        
        # Between min and max the total gap is (max - min) and there are (N-1) slots
        # The average gap per slot is (max - min)/(N-1), this might be a double value
        # The max gap must be >= ceiling[(max - min)/(N-1)]
        