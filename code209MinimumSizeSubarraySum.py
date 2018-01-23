"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        res, sum = 0, 0
        for j in range(len(nums)):
            sum += nums[j]
            if sum >= s:
                while sum >= s:
                    sum -= nums[i]
                    i += 1
                if res == 0:
                    res = j - i + 2
                else:
                    res = min(res, j - i + 2)

        return res

test_case = [1, 1,1, 1,1, 1,1, 4]
obj = Solution()
print(obj.minSubArrayLen(7, test_case))