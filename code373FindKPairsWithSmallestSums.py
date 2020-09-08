"""
373 Find K Pairs with Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3 

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
"""
from heapq import *
class Solution:
    # K*log(K) solution, easier to understand
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        if m < 1 or n < 1 or k < 1: return []
        
        # if k < m, then we don't need nums1[k] because nums1[0...k-1] with nums2[0] will form k smaller pairs than nums1[k] and nums2[0]
        q = [(nums1[i] + nums2[0], i, 0) for i in range(min(m, k))]
        heapify(q)
        res = []
        while k and q:
            val, i, j = heappop(q)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heappush(q, (nums1[i] + nums2[j+1], i, j+1))
            k -= 1
        return res

    # https://www.cnblogs.com/grandyang/p/5653127.html
    def kSmallestPairs3(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        res, idx = [], [0]*m
        for _ in range(min(k, m*n)):
            cur, _sum = 0, 2**31-1
            for i in range(m):
                if idx[i] < n and _sum >= nums1[i] + nums2[idx[i]]:
                    cur = i
                    _sum = nums1[i] + nums2[idx[i]]
            
            res.append((nums1[cur], nums2[idx[cur]]))
            idx[cur] += 1

        return res

    # https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84551/simple-Java-O(KlogK)-solution-with-explanation
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(nums1), len(nums2)
        if m < 1 or n < 1 or k < 1:
            return []

        res = []
        queue = []
        for i in range(min(k, m)):
            heappush(queue, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))   # tuple (sum of num1 and num2, num1, num2, current nums2's index)
        
        while k > 0 and len(queue) > 0:
            t = heappop(queue)
            res.append([t[1], t[2]])
            if t[3] < n-1:
                heappush(queue, (t[1] + nums2[t[3] + 1], t[1], nums2[t[3] + 1], t[3] + 1))
            # think why we don't need to push additional items into min_heap if t[3] >= n-1?
            k -= 1
        
        return res

    # first solution, doesn't work for nums1 = [1, 1, 2], nums2 = [1,2,3]
    # the idea is to limit the first element in neighboring indices, e.g., comparing nums1[i] + nums2[p] and nums1[i+1] + nums2[q]
    # then advance p or q accordingly.Doesn't work for nums1 = [1, 1, 2], nums2 = [1,2,3]
    def kSmallestPairs2(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(nums1), len(nums2)
        if m < 1 or n < 1 or k < 1:
            return []

        res = []
        i, p, q = 0, 0, 0
        while i < m-1 and len(res) < k:
            first, second = nums1[i] + nums2[p], nums1[i+1] + nums2[q]
            if first <= second:
                res.append([nums1[i], nums2[p]])
                p += 1
                if p == n:
                    i += 1
                    p = q
                    q = 0
            else:
                res.append([nums1[i+1], nums2[q]])
                q += 1
                # q will never achieve n first because nums1[i] + nums2[-1] <= nums1[i+1] + nums2[-1]
        
        while p < n and len(res) < k:
            res.append([nums1[i], nums2[p]])
            p += 1
        
        return res

obj = Solution()
nums1 = [1,1, 2]
nums2 = [1,2,3]
print(obj.kSmallestPairs3(nums1, nums2, 9))
