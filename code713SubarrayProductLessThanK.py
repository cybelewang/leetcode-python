"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""
from bisect import bisect_left
class Solution:
    # my own solution using accumulated product array and binary search
    # this is not a correct solution because the problem requires contiguous subarrays
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        # get accumulated product array
        product = [nums[0]]
        for i in range(1, n):
            product.append(product[-1]*nums[i])

        res = 0
        # find the position end where nums[end-1] is the largest number that smaller than k
        end = bisect_left(nums, k)
        for i in range(end-1, -1, -1):
            # count number of subarrays that end with nums[i] and their product < k
            length = bisect_left(product, k // nums[i], 0, i)
            res += 2**length    # for length nubers, they have 2^length subsets
        
        return res

nums, k = [10, 5, 2, 6], 100
print(Solution().numSubarrayProductLessThanK(nums, k))