"""
238 Product of Array Except Self

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

    # follow-up: print the result in terminal, no need to use an array (FB interview question)
    # First analyze the input array: if there are two zeros, all output will be zero
    # if there is only one 0, then all other places are 0 except the place with zero
    # if there is no 0, we calculate all product and divide it by the number
    def productExceptSelf_divide(self, nums):
        zeroCnt = nums.count(0)
        # more than 1 zero, all result must be 0
        if zeroCnt > 1:
            for num in nums: print(0)
            return
        # only one 0 exists
        if zeroCnt == 1:
            for i in len(nums):
                if nums[i] != 0: print(0)
                else:
                    p = 1
                    for j in range(len(nums)):
                        if nums[j] != 0:
                            p *= nums[j]
                    print(p)
            return
        # no zero exists
        p = 1
        for num in nums:
            p *= num
        
        for num in nums:
            print(p//num)

obj = Solution()
test_case = [6, 8]
print(obj.productExceptSelf(test_case))
obj.productExceptSelf_divide(test_case)