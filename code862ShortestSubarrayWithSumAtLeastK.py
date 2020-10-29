"""
862 Shortest Subarray with Sum at Least K

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
If there is no non-empty subarray with sum at least K, return -1.
 

Example 1:
Input: A = [1], K = 1
Output: 1
Example 2:
Input: A = [1,2], K = 4
Output: -1
Example 3:
Input: A = [2,-1,2], K = 3
Output: 3
 
Note:
1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
"""
from heapq import heappush, heappop
from collections import deque
class Solution:
    def shortestSubarray(self, A, K):
        n, res = len(A), 50001
        sums = [0]
        for a in A: sums.append(sums[-1] + a)
        q = deque([0])
        for i in range(1, n+1):
            while q and sums[i] - sums[q[0]] >= K:
                res = min(res, i - q[0])
                q.popleft()
            while q and sums[q[-1]] >= sums[i]:
                q.pop()
            q.append(i)
        
        return res if res != 50001 else -1

    # Use a minHeap to save the accumulation sum, O(NlogN)
    # for each current accumulation sum, pop the min previous accumulation sum from minHeap and then update the result
    def shortestSubarray2(self, A, K):
        sums = [0]
        for num in A: sums.append(sums[-1] + num)
        q = [(0, 0)] # minHeap contains tuples of (sum, length)
        res = 2**31-1 # result
        for i in range(1, len(sums)):
            while q and sums[i] - q[0][0] >= K: # bug fixed: must check if q is empty
                res = min(res, i-heappop(q)[1])
            heappush(q, (sums[i], i))
        
        return res if res != 2**31-1 else -1