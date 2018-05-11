"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""
from bisect import bisect_left
class Solution:
    # Wrong solution. Target number sum(nums)//2 is not necessarily to be the sum beginning from smallest number.
    def canPartition2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        
        # sort the input
        nums.sort()
        # get the sums array
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        # if the total sum of list is odd, return False
        if (nums[-1] % 2)&1:
            return False

        # binary search the half of total sum
        index = bisect_left(nums, nums[-1]//2)
        # check if the half of total sum exists
        return nums[index] == (nums[-1]//2)

obj = Solution()
print(obj.canPartition2([1, 2, 3, 4, 6]))
