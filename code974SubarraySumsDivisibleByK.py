"""
974 Subarray Sums Divisible by K

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""
class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: list[int]
        :type K: int
        :rtype: int
        """
        remains = [0]*K
        remains[0] = 1

        rem = 0
        for a in A:
            rem = (rem + a) % K
            remains[rem] += 1
        
        res = 0
        for cnt in remains:
            res += (cnt-1)*cnt//2
        
        return res

A = [2, 0, 2]
K = 2
print(Solution().subarraysDivByK(A, K))