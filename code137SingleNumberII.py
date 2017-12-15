"""
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
# count bit at the same position, and module by 3
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0]*32  # count of corresponding bit '1's in 32-bit integers
        for num in nums:
            for i in range(32):
                if num%2 != 0:
                    count[i] += 1
                num //=2
        
        res = 0
        for i in range(32):
            res = 2*res + count[31-i]%3
        
        return res

test_case = [1,1,3,2,1,2,2,3,3]
obj = Solution()
print(obj.singleNumber(test_case))