"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

"""
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res, p, n = [], 1, len(nums)
        for num in nums:
            res.append(p)
            p *= num

        p = 1
        for j in range(n-1, -1, -1):
            res[j] *= p
            p *= nums[j]
        
        return res

obj = Solution()
test_case = [6, 8]
print(obj.productExceptSelf(test_case))