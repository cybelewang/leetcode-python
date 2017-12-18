"""
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
# count bit at the same position, and module by 3
# python solution not accepted because python uses long type int. better to do this with java or C++
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0]*32  # count of corresponding bit '1's in 32-bit integers
        for num in nums:
            for i in range(32):
                if (num & (1<<i)) != 0:
                    count[i] += 1
        
        res = 0
        for i in range(32):
            if count[i]%3 !=0:
                res |= (1 << i)
        
        return res

test_case = [1,1,1,2,2,2,3]
obj = Solution()
print(obj.singleNumber(test_case))