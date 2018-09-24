"""
719 Find K-th Smallest Pair Distance

Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
"""
# similar problems: 373 Find K Pairs with Smallest Sums; 378 Kth Smallest Element in a Sorted Matrix; 658 Find K Closet Elements; 668 Kth Smallest Number in Multiplication Table; 786 K-th Smallest Prime Fraction
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/8627783.html
    # binary search in a 2D array
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n, left, right = len(nums), 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right)//2

            # count number of distances that are <= mid
            cnt, start = 0, 0
            for i in range(n):
                while start < i and nums[i] - nums[start] > mid:
                    start += 1
                cnt += i - start
            
            if cnt < k: # mid is too small
                left = mid + 1
            else:   # mid is large
                right = mid
        
        return right

nums = [3, 2, 1, 3, 5]
print(Solution().smallestDistancePair(nums, 3))
