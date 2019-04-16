"""
1027 Longest Arithmetic Sequence

Given an array A of integers, return the length of the longest arithmetic subsequence in A.
Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, 
and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

Example 1:
Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.

Example 2:
Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].

Example 3:
Input: [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].

Note:

2 <= A.length <= 2000
0 <= A[i] <= 10000
"""
from collections import defaultdict
class Solution:
    # use method from 446 Arithmetic Slices II - Subsequence
    # O(N^2) time, O(N^2) space
    def longestArithSeqLength(self, A):
        """
        :type A: list[int]
        :rtype: int
        """
        res, n = 0, len(A)
        dp = [defaultdict(int) for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = 1 + dp[j][diff]   # Append A[i] after A[j]
                else:
                    dp[i][diff] = 2 # initial length is 2
                res = max(res, dp[i][diff])
        
        return res

A = [20,1,15,3,10,5,8]  # expect 4
A = [3, 6, 9, 12]   # expect 4
A = [1, 2, 4, 5, 7, 8, 9]   # expect 3
print(Solution().longestArithSeqLength(A))