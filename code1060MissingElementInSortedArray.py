"""
1060 Missing Element in Sorted Array

Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array. 

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
"""
class Solution:
    # skip calculation: nums[i] - nums[0] - i
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        fullskip = nums[-1] - nums[0] + 1 - n
        if fullskip < k: return nums[-1] + k - fullskip
        
        # binary search the first index whose skip >= k
        left, right = 0, n
        while left < right:
            mid = (left + right)//2
            skip = nums[mid] - nums[0] - mid
            if skip < k:
                left = mid + 1
            else:
                right = mid

        # need to backward right to find the result
        right -= 1
        skip = nums[right] - nums[0] - right
        return nums[right] + k - skip
        