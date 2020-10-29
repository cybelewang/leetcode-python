"""
264 Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
"""
from heapq import heappush, heappop
# a competition algorithm, the minimun of previous ugly number times with 2, 3, 5 will be the next number
# every ugly number needs to time 2, 3, 5 and contributes to next ugly number
# see excel for detailed explanation
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            raise ValueError
        
        k = [1]*n
        t2, t3, t5 = 0, 0, 0    # t2: available ugly number's index which can time 2 and possibly contribute to next ugly number
        for i in range(1, n):
            k[i] = min(k[t2]*2, k[t3]*3, k[t5]*5)
            if k[i] == k[t2]*2:
                t2 += 1
            if k[i] == k[t3]*3:
                t3 += 1
            if k[i] == k[t5]*5:
                t5 += 1
        
        return k[-1]

    # minHeap solution
    def nthUglyNumber(self, n: int) -> int:
        q, res = [1], 1
        for _ in range(n):
            t = heappop(q)
            res = t
            while q and q[0] == t:
                heappop(q)
            heappush(q, t*2)
            heappush(q, t*3)
            heappush(q, t*5)
        return res

obj = Solution()
print(obj.nthUglyNumber(10))