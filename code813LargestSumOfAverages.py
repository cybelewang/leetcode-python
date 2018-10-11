"""
813 Largest Sum of Averages

We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. 
What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input: 
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation: 
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
 

Note:

1 <= A.length <= 100.
1 <= A[i] <= 10000.
1 <= K <= A.length.
Answers within 10^-6 of the correct answer will be accepted as correct.
"""
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/9504413.html
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        n = len(A)
        sums = [0]*(n+1)    # sums[i] is the sum of first length-i elements
        for i in range(n):
            sums[i+1] = sums[i] + A[i]
        
        dp = [[0.0]*n for _ in range(n)]    # dp[i][k] is the max average sum in range [i, n-1], up to k groups
        dp[i][0] = (sums[n] - sums[i])/(n-i)    # no group, just calculate the average of the whole array

        for k in range(1, K):
            for i in range(n-1):
                for j in range(i+1, n):
                    dp[i][k] = max(dp[i][k], (sums[j] - sums[i])/ (j-i) + dp[j][k-1])
        
        return dp[0][K-1]