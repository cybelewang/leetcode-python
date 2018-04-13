"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from heapq import *
class Solution:
    # hashmap + maxHeap
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hist = {}
        for num in nums:
            if num not in hist:
                hist[num] = 0
            hist[num] += 1

        freq_num = [(-v, key) for (key, v) in hist.items()]
        heapify(freq_num)

        res = []
        for i in range(k):
            res.append(heappop(freq_num)[1])

        return res

test_case = [1, 1, 1, 2, 2, 3]
obj = Solution()
print(obj.topKFrequent(test_case, 2))