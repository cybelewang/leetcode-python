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
    # binary search solution, time O(nlogn)
    # https://www.cnblogs.com/grandyang/p/4938187.html
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, cnt = [], 0
        for num in nums:
            p = bisect_left(a, num)
            if p == len(a):
                a.append(num)
            else:
                a[p] = num

        return len(a)

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
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
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

    # Follow-up: output all longest LISs
    # Use DFS
    def getLIS(self, nums):
        self.maxLen = 0
        def dfs(nums, start, build, res):
            if start == len(nums):
                # update res if necessary
                if len(build) > self.maxLen:
                    self.maxLen = len(build)
                    res.clear()
                    res.append(build[:])
                elif len(build) == self.maxLen:
                    res.append(build[:])
                return

            # trim some invalid cases
            if len(build) + len(nums) - start < self.maxLen:
                return

            # two cases: use nums[i] or do not use nums[i]
            i = start
            # append this number and continue dfs
            if not build or nums[i] > build[-1]:
                build.append(nums[i])
                dfs(nums, i+1, build, res)
                build.pop()
            # abandon this number and continue dfs, this replaces for loop in typical DFS
            dfs(nums, i+1, build, res)        

        res = []
        dfs(nums, 0, [], res)
        return res

    def getLIS2(self, nums):
        self.maxLen = 0
        def dfs(nums, start, build, res):
            if start == len(nums): return

            # trim some invalid cases
            if len(build) + len(nums) - start < self.maxLen:
                return

            for i in range(start, len(nums)):
                # try to append this number and continue dfs
                if not build or nums[i] > build[-1]:
                    build.append(nums[i])
                    # update res if necessary
                    if len(build) > self.maxLen:
                        self.maxLen = len(build)
                        res.clear()
                        res.append(build[:])
                    elif len(build) == self.maxLen:
                        res.append(build[:])
                    # continue dfs
                    dfs(nums, i+1, build, res)
                    build.pop()

        res = []
        dfs(nums, 0, [], res)
        return res

test_case = [10, 9, 2, 5, 3, 7, 101, 18]
#test_case = [1, 3, 2]
obj = Solution()
print(obj.lengthOfLIS3(test_case))
print(obj.getLIS2(test_case))