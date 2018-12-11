"""
907 Sum of Subarray Minimums

Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000
"""
class Solution:
    def sumSubarrayMins_TLE(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans, M, N = 0, 1000000007, len(A)
        dp = [30001]*N

        for i in range(N):
            for j in range(i+1):
                dp[j] = min(dp[j], A[i])
                ans = (ans + dp[j]) % M

        return ans

A = [3,1,2,4]
print(Solution().sumSubarrayMins(A))