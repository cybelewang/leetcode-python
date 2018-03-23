"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""
class Solution:
    # brutal force
    def lengthOfLIS(self, nums):
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
print(obj.lengthOfLIS(test_case))