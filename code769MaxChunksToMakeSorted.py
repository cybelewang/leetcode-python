"""
769 Max Chunks To Make Sorted

Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
Note:

arr will have length in range [1, 10].
arr[i] will be a permutation of [0, 1, ..., arr.length - 1].
"""
# similar problems: 45 Jump Game II
class Solution:
    # my own solution inspired by finding 0's position idx0, then numbers from position 0 to position idx0 must be in a chunk because 0 will be sorted to position 0
    # after finding 0's position idx0, we will iterate i from position 0 to idx0, for arr[i], we will find its position index[arr[i]], and if it's larger than idx0, we must extend the end 
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        index = {a:i for i, a in enumerate(arr)}

        start, res = 0, 0
        while start < len(arr):
            i, end = start, index[start]
            while i <= end: # iterate until all numbers' index are within [start, end]
                end = max(end, index[arr[i]])
                i += 1
            # update start for next chunk
            start = end + 1
            res += 1

        return res

arr = [4,3,2,1,0]
print(Solution().maxChunksToSorted(arr))