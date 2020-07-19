"""
368 Largest Divisible Subset

Given a set of distinct positive integers, find the largest subset such that every pair (S_i, S_j) of elements in this subset satisfies: S_i % S_j = 0 or S_j % S_i = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
"""
class Solution:
    # https://leetcode.com/problems/largest-divisible-subset/discuss/84002/4-lines-in-Python
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = {1:[]}   # key: number, value: a list of divisible subset <= x
        for x in sorted(nums):
            s[x] = max((s[d] for d in s if x % d == 0), key=len) + [x]
        return list(max(s.values(), key=len))

nums = [1, 2, 3, 4, 6, 8]
print(Solution().largestDivisibleSubset(nums))