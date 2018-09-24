"""
480 Sliding Window Median

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note: 
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
"""
# similar problem 295
from bisect import bisect_left, insort_left
class Solution:
    # reference http://zxi.mytechroad.com/blog/difficulty/hard/leetcode-480-sliding-window-median/
    # also need to see other C++'s multiset solution
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window = sorted(nums[:k])
        res = []
        for i in range(k, len(nums)+1):
            res.append((window[k//2] + window[(k-1)//2])/2.0)   # trick to get the median: for odd k, k//2 and (k-1)//2 are the same, for even k, k//2 and (k-1)//2 are different
            if i == len(nums):
                break
            index = bisect_left(window,nums[i-k])   # find the left item's index in the window O(logk)
            window.pop(index)   # remove the left item O(k)
            insort_left(window, nums[i])    # insert the right item into the window O(logk)

        return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().medianSlidingWindow(nums, k))    
