"""
313 Super Ugly Number

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. 
For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""
from heapq import heappush, heappop
# similar to 264
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = len(primes)
        # test this corner case
        if k == 0 or n < 1:
            return 1

        if primes[0] == 1:
            primes = primes[1:]

        index = [0]*k
        
        uglyNums = [1]*n
        for i in range(1, n):
            uglyNums[i] = 2**31 - 1
            for j in range(k):
                uglyNums[i] = min(uglyNums[i], uglyNums[index[j]]*primes[j])
            
            for j in range(k):
                if uglyNums[i] == uglyNums[index[j]]*primes[j]:
                    index[j] += 1

        return uglyNums[-1]

    # minHeap solution
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        q = [1]
        res = 1
        for _ in range(n):
            res = heappop(q)
            while q and q[0] == res:
                heappop(q)
            for p in primes:
                heappush(q, res*p)
        
        return res

obj = Solution()
print(obj.nthSuperUglyNumber(12, [2, 7, 13, 19]))