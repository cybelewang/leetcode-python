"""
347 Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from heapq import *
class Solution:
    # hashmap + maxHeap, O(N + KlogN)
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

    # Quick sort's partition method, average O(N), worst O(N^2)
    # similar to C++'s nth_element    
    def topKFrequent2(self, nums, k):
        count = Counter(nums)
        def partition(arr, s, e):
            i = s
            for j in range(s, e):
                if count[arr[j]] < count[arr[e]]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i], arr[e] = arr[e], arr[i]
            return i
        
        arr = list(count.keys())
        n = len(arr)
        left, right = 0, len(arr)-1
        while left <= right:
            i = partition(arr, left, right)
            if n-i == k:
                return arr[i:]
            elif n-i < k:
                right = i - 1
            else:
                left = i + 1
             

test_case = [1, 1, 1, 2, 2, 3]
obj = Solution()
print(obj.topKFrequent(test_case, 2))