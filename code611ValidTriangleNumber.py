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
# similar problems: 259 3Sum Smaller
from bisect import bisect_left
class Solution:
    # Solution 2 from http://www.cnblogs.com/grandyang/p/7053730.html, O(n^2)
    # sort nums, then iterate from the end of nums with index i
    # intitalize left = 0, right = i - 1, then check if nums[left] + nums[right] > nums[i], if so, all numbers between left and right - 1 will be fit
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n, res = len(nums), 0
        for i in range(n-1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
            
        return res

    # my own solution, using binary search O(n^2logn)
    def triangleNumber2(self, nums):
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

        for i in range(n-2):
            a = nums[i]
            for j in range(i+1, n-1):
                b = nums[j]
                index = bisect_left(nums, a+b, j+1) # pitfall here: we should search from index j+1, because numbers with index <= j have already been included in previous loops
                res += index - j - 1
        
        return res

nums = [3,4,5,5]        
print(Solution().triangleNumber(nums))
