"""
239 Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""
# similar problems: 480 Sliding Window Median
# follow up: Sliding Window Minimum
from math import log2, ceil
from collections import deque
class Solution:
    # Deque method, from java solution
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q, res = deque(), []
        for (i, num) in enumerate(nums):
            while len(q) > 0 and q[0] < i - k + 1:  # remove out of range elements
                q.popleft()
            
            while len(q) > 0 and nums[q[-1]] <= num: # remove elements which are smaller than current one
                q.pop()

            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])  # the most left element must be in range, and not smaller than any remaining element in the deque

        return res

    # Two direction solution in https://leetcode.com/problems/sliding-window-maximum/solution/
    # Divide the array into different buckets, and each bucket has size k (last bucket may have smaller size).
    # Then we generate two arrays: left[i] is the max from bucket_left to [i], and right[i] is the max from bucket_right to [i]
    # Then for each window start with i and end with j, the max will be max(right[i], left[j])
    def maxSlidingWindow2(self, nums, k):
        INT_MIN = -2**31
        n = len(nums)
        left, right = [INT_MIN]*n, [INT_MIN]*n
        # generate the bucket max list that represents the max from bucket_left to this index (inclusive)
        pre = INT_MIN
        for i, num in enumerate(nums):
            pre = max(pre, num)
            left[i] = pre
            if (i+1)%k == 0:
                pre = INT_MIN
        # generate the bucket max list that represents the max from bucket_right to this index (inclusive)
        pre = INT_MIN
        for j in range(n-1, -1, -1):
            if (j+1)%k == 0:
                pre = INT_MIN
            pre = max(pre, nums[j])
            right[j] = pre
        # combine the left and right list to get the result
        # for a window with start index i and end index j, the result will be max(right[i], left[j])
        res = []
        for j in range(k-1, n):
            i = j-k+1
            res.append(max(right[i], left[j]))
        return res

    # Segment Tree solution
    def maxSlidingWindow3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # construct segment tree
        def constructSegmentTree(arr, s, e, st, i):
            """            
            arr: the input array, whose elements will be leaves of the result segment tree
            s: start index in arr
            e: end index in arr
            st: the segment tree in array form
            i: index of segment tree
            return: the max value in the segment
            """
            if s == e:
                st[i] = arr[s]
                return arr[s]
            
            mid = (s + e)//2
            st[i] = max(constructSegmentTree(arr, s, mid, st, 2*i+1), constructSegmentTree(arr, mid+1, e, st, 2*i+2))

            return st[i]

        # query the max value in a given range
        def query(st, i, s, e, qs, qe):
            """
            st: the segment tree in array form
            i: current index in segment tree
            s: start index in arr
            e: end index in arr
            qs: query start index in arr
            qe: query end index in arr
            return: the max value in arr[s to e]
            """
            if qs <= s and qe >= e: # [s to e] in range [qs to qe] 
                return st[i]

            if qs > e or qe < s: # [s to e] is completely out of range [qs to qe]
                return -2**31

            mid = (s + e)//2

            return max(query(st, 2*i + 1, s, mid, qs, qe), query(st, 2*i + 2, mid+1, e, qs, qe))

        
        # calculate the size of segment tree
        n = len(nums)
        if n < 1:
            return []

        h = ceil(log2(n))
        N = 2**(h+1) - 1

        # construct the segment tree
        st = [0 for i in range(N)]
        constructSegmentTree(nums, 0, n-1, st, 0)

        res = []
        for i in range(n-k+1):
            res.append(query(st, 0, 0, n-1, i, i+k-1))

        return res

obj = Solution()
nums = [1,3,-1,-3,5,3,6,7]
print(obj.maxSlidingWindow2(nums, 3))