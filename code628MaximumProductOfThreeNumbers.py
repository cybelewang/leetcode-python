"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,10^4] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""
# similar problems: 152 Maximum Product Subarray
class Solution:
    # my own solution. 
    # keep two arrays, max2 tracks the max product of any two numbers before nums[i], min2 tracks the min product of any two numbers before nums[i]
    # The max three product must be max of max2[i-1]*nums[i] and min2[i-1]*nums[i]
    # max2 and min2 can be achieved using the similar way as shown below
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # get the max product and min product of two numbers
        max2, min2 = [0]*n, [0]*n
        max_left, min_left = nums[0], nums[0]
        for i in range(1, n-1):
            a, b = max_left*nums[i], min_left*nums[i]
            max2[i] = max(a, b)
            min2[i] = min(a, b)
            max_left = max(max_left, nums[i])
            min_left = min(min_left, nums[i])
        
        print(max2)
        print(min2)
        # the final result will be either max2_left * nums[i], or min2_left * nums[i]
        res = -2**31
        for i in range(2, n):
            p = max(max2[i-1]*nums[i], min2[i-1]*nums[i])
            res = max(res, p)

        return res

nums = [-4,-3,-2,-1,60] # expected: 720
print(Solution().maximumProduct(nums))
