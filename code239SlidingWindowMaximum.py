"""
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
            
            while len(q) > 0 and nums[q[-1]] < num: # remove elements which are smaller than current one
                q.pop()

            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])  # the most left element must be in range, and not smaller than any remaining element in the deque

        return res

    # Segment Tree solution
    def maxSlidingWindow2(self, nums, k):
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
print(obj.maxSlidingWindow(nums, 3))