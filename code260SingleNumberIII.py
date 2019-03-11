"""
260 Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
# https://leetcode.com/problems/single-number-iii/discuss/68900/Accepted-C++Java-O(n)-time-O(1)-space-Easy-Solution-with-Detail-Explanations
# first xor all numbers, and the result is diff
# then take any isolated bit 1 from diff and form a "signature" number
# use that "signature" number to distinguish nums into two groups: one group with all numbers has that bit 1, one group with all numbers with that bit 0
# The same numbers must fall into one group, only the two result numbers are in two different group
# xor the two groups and we will get the final result
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res, diff = [0, 0], 0
        for num in nums:
            diff ^= num

        # isolate the most right set bit
        diff &= -diff
        for num in nums:
            if (num & diff) == 0:
                res[0] ^= num
            else:
                res[1] ^= num
                      
        return res 

obj = Solution()
nums = [1, 2, 1, 3, 2, 5]
print(obj.singleNumber(nums))