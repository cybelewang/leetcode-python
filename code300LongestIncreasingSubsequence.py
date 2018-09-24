"""
300 Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""
from collections import deque
from bisect import *
class Solution:
    # dp solution, time O(nlogn)
    # https://leetcode.com/problems/longest-increasing-subsequence/solution/
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 1:
            return 0

        dp = [0]*n
        maxLen = 0
        for num in nums:
            i = bisect_left(dp, num, 0, maxLen)
            dp[i] = num
            #print(dp)
            if i == maxLen:
                maxLen += 1
        
        return maxLen

    # dp solution, time O(n^2)
    # for current index i, we iterate j from 0 to i-1 (included)
    # if nums[i] > nums[j], this means we can form a longer increasing subsequence by appending nums[i]
    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 1:
            return 0

        dp = [1]*n
        for i in range(1, n):
            maxLen = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxLen = max(maxLen, dp[j])
            dp[i] = maxLen + 1
        
        return max(dp)

    # TLE
    # Graph + BFS, my own solution, time O(n^2)
    def lengthOfLIS3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0

        # create graph
        graph = []
        for i in range(len(nums)):
            connections = []    # connections contain index of the numbers > nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    connections.append(j)
            graph.append(connections)
        
        queue = deque()
        queue.extend(range(len(nums)))  # start from all possible numbers

        level = 0
        while len(queue) > 0:
            level += 1
            size = len(queue)
            for i in range(size):
                start = queue.popleft()
                for j in graph[start]:
                    queue.append(j)
        
        return level


    # brutal force, will cause TLE
    def lengthOfLIS4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def _numOfLarge(nums, start):
            count = 1
            for i in range(start + 1, len(nums)):
                if nums[i] > nums[start]:
                    count = max(count, 1 + _numOfLarge(nums, i))
            return count

        res = 0
        for i in range(len(nums)):
            res = max(res, _numOfLarge(nums, i))

        return res

test_case = [10, 9, 2, 5, 3, 7, 101, 18]
obj = Solution()
print(obj.lengthOfLIS3(test_case))