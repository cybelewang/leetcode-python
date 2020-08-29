"""
644 Maximum Average Subarray II

Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
Note:
1 <= k <= n <= 10,000.
Elements of the given array will be in range [-10,000, 10,000].
The answer with the calculation error less than 10-5 will be accepted.
"""
class Solution:
    # binary search method
    # https://www.cnblogs.com/grandyang/p/8021421.html
    def findMaxAverage(self, nums, k):
        left, right = min(nums), max(nums)
        while right - left > 1e-5:
            mid = (left + right)/2.0
            minSum, su, preSum = 0.0, 0.0, 0.0
            check = False
            for i in range(len(nums)):
                su += nums[i] - mid
                if i >= k:
                    preSum += nums[i-k] - mid # preSum of nums[:i-k+1] - mid
                    minSum = min(minSum, preSum) # min of preSum
                if i >= k-1 and su > minSum: # if su > min of preSum, this means we have found a subarray with size >= k and its diff sum > 0
                    check = True
                    break
            if check:
                # mid is too small, we need to increase it
                left = mid
            else:
                # mid is too large, we need to decrease it
                right = mid
        
        return left

    # 8/24/2020
    # The trick is how to write the check function in O(N) time complexity
    def findMaxAverage2(self, nums: List[int], k: int) -> float:
        n = len(nums)

        # O(N) sliding window check
        # su is the diff sum of (nums[:i+1] - avg)
        # preSum is the diff sum of (nums[:i-k+1] - avg)
        # minPreSum is the min of all preSum
        # if su > minPresum, this means we find a subarray with length >= k, and average > avg
        def check(avg):
            su, preSum, minPreSum = 0, 0, 0
            for i in range(n):
                su += nums[i] - avg
                if i >= k:
                    preSum += nums[i-k] - avg
                    minPreSum = min(minPreSum, preSum)
                if i >= k-1:
                    if su > minPreSum:
                        return False
            return True
        
        left, right = min(nums), max(nums)
        while right - left > 1e-5:
            mid = (left + right) / 2.0
            if check(mid):
                right = mid
            else:
                left = mid
                
        return left       

print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4)) # expect 12.75