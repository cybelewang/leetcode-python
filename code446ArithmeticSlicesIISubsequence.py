"""
446 Arithmetic Slices II - Subsequence


A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array is any sequence of integers (P_0, P_1, ..., P_k) such that 0 ≤ P_0 < P_1 < ... < P_k < N.

A subsequence slice (P_0, P_1, ..., P_k) of array A is called arithmetic if the sequence A[P_0], A[P_1], ..., A[P_k-1], A[P_k] is arithmetic. In particular, this means that k ≥ 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -2^31 and 2^31-1 and 0 ≤ N ≤ 1000. The output is guaranteed to be less than 2^31-1.


Example:

Input: [2, 4, 6, 8, 10]

Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
"""
from collections import defaultdict
class Solution:
    # http://www.cnblogs.com/grandyang/p/6057934.html
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        # dp[i] is a dict. Key is the difference between A[i] and any previous number A[0:i] (i excluded), value is the number of slices with each slice ending with A[i]
        dp = [defaultdict(int) for _ in range(n)]   # pitfall: cannot use [defaultdict(int)]*n
        res = 0

        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] += 1    # one more slice with difference "diff" and ends with A[i]
                if diff in dp[j]:
                    res += dp[j][diff]
                    dp[i][diff] += dp[j][diff]  # The previous slices ending with A[j] can form new slices ending with A[i]

                # or use below code
                # dp[i][diff] += 1 + dp[j][diff]    # should not use dp[i][diff] = 1 + dp[j][diff] because diff may already exist
                # res += dp[j][diff]
        
        return res

A = [2, 2, 3, 4]
obj = Solution()
print(obj.numberOfArithmeticSlices(A))