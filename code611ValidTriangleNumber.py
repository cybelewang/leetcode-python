"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""
from bisect import bisect_left
class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort nums
        nums.sort()
        start, n = 0, len(nums)
        while start < n and nums[start] == 0:
            start += 1

        nums = nums[start:]
        res = 0

        for i in range(n-1):
            a = nums[i]
            for j in range(i+1, n):
                b = nums[j]
                index = bisect_left(nums, a+b)
                
                
