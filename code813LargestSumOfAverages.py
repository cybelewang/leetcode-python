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
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        N, sums = len(A), [0]
        for a in A: sums.append(sums[-1] + a)
        # initially dp[i] represents the max average sum of A[:i] on 1 group
        dp = [0]*(N+1)
        for i in range(1, N+1):
            dp[i] = sums[i] / i
        
        # we need to iterate from 2 group because 1 group calculation has been completed
        for i in range(2, K+1):
            dp[0] = 0
            for j in range(N, 0, -1): # use reverse iteration because we need previous dp value
                for p in range(i-1, j):
                    dp[j] = max(dp[j], dp[p] + (sums[j] - sums[p]) / (j - p))
        
        return dp[N]

    # DFS + Cache solution
    def largestSumOfAverages3(self, A, K):
        sums = [0]
        for a in A: sums.append(sums[-1] + a)
        
        # backtracking function to return max average sum of A[start:] in groups
        def helper(start, groups, mem):
            if groups == 1: return (sums[-1] - sums[start])/(len(A) - start) # bug fixed: should not just return sum
            if (start, groups) in mem: return mem[(start, groups)] # cache hit
            # cache not hit, calculate the max average sum of A[start:]
            res = 0
            for i in range(start+1, len(A) - groups + 2): # i is the end (exclusive) of current group, and we need to allocate remain groups = (groups - 1)
                res = max(res, (sums[i] - sums[start])/(i-start) + helper(i, groups-1, mem))
            
            mem[(start, groups)] = res
            return res
        
        return helper(0, K, {})

    # help from http://www.cnblogs.com/grandyang/p/9504413.html
    def largestSumOfAverages2(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        n = len(A)
        sums = [0]*(n+1)    # sums[i] is the sum of first length-i elements
        for i in range(n):
            sums[i+1] = sums[i] + A[i]
        
        dp = [[0.0]*K for _ in range(n)]    # dp[i][k] is the max average sum in range [i, n-1], up to k groups
        for i in range(n):
            dp[i][0] = (sums[n] - sums[i])/(n-i)    # 1 group, just calculate the average of the whole array

        for k in range(1, K):
            for i in range(n-1):
                for j in range(i+1, n):
                    dp[i][k] = max(dp[i][k], (sums[j] - sums[i])/ (j-i) + dp[j][k-1])
        
        return dp[0][K-1]

A = [4,1,7,5,6,2,3]
K = 4   # expected 18.16667
print(Solution().largestSumOfAverages(A, K))