"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
class Solution:
    # improved solution from http://www.cnblogs.com/grandyang/p/7722949.html
    # two maps, one pass
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, count = {}, {}
        degree, res = 0, len(nums)
        for i, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1
            if num not in start:
                start[num] = i
            if count[num] == degree:
                res = min(res, i - start[num] + 1)
            elif count[num] > degree:
                degree = count[num]
                res = i - start[num] + 1    # bug fixed: should not use res = min(res, i - start[num] + 1)
        
        return res

    # my own two-pass solution using two maps, a set
    def findShortestSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, count = {}, {}
        for i, num in enumerate(nums):
            if num not in start:
                start[num] = i
            count[num] = count.get(num, 0) + 1
        
        degree = max(count.values())
        candidates = set(num for num in count if count[num]==degree)

        res = len(nums)
        for i, num in enumerate(nums):
            count[num] -= 1
            if num in candidates and count[num] == 0:
                res = min(res, i - start[num] + 1)
        
        return res

nums = [1,2,2,3,1,4,2]
print(Solution().findShortestSubArray(nums))