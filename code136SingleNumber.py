"""
136 Single Number

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
# xor operation between two identical numbers will result 0
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num

        return res

test_case = [1, 2,1, 3,2,7, 3]
obj = Solution()
print(obj.singleNumber(test_case))