"""
768 Max Chunks To Make Sorted II

This question is the same as "Max Chunks to Make Sorted" except the integers of the given array are not necessarily distinct, the input array could be up to length 2000, and the elements could be up to 10**8.

Given an array arr of integers (not necessarily distinct), we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
Note:

arr will have length in range [1, 2000].
arr[i] will be an integer in range [0, 10**8].
"""
from bisect import bisect_right
class Solution:
    # OJ best
    # compare the prefix sum and see if they are equal
    def maxChunksToSorted(self, A):
        res, s1, s2 = 0, 0, 0
        for a, b in zip(A, sorted(A)):
            s1 += a
            s2 += b
            res += s1 == s2
        return res
        
    # my own solution to keep intervals in result list. time O(NlogN), space O(N)
    # Assume we have a result list which contains intervals in ascending orders, like [[1, 2], [3, 5], [6, 7]]
    # Now if we want to insert a new number, we first find the right insert index idx using binary search
    # Then we should remove all intervals from idx to list end because these intervals should be in a single chunk now
    # if num can be merged to previous interval (chunk), we do so
    # otherwise we append a new interval with [num, end], where end is the largest number on arr[idx:]
    def maxChunksToSorted(self, arr: List[int]) -> int:
        order = []
        for num in arr:
            idx = bisect_right(order, [num, num])
            end = num
            while len(order) > idx:
                erased = order.pop()
                end = max(end, erased[1])
            if idx > 0 and order[idx-1][1] > num:
                order[idx-1][1] = max(order[idx-1][1], end)
            else:
                order.append([num, end])
        print(order)
        return len(order)