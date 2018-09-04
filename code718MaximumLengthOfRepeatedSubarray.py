"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""
# similar problems: 583, 712
class Solution:
    # my improved solution using O(n) space, note we must iterate from end to begin so when dp[j] = 1 + dp[j-1], dp[j-1] remains the last-i number
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m, n = len(A), len(B)
        dp = [0]*(n+1)

        res = 0
        for i in range(1, m+1):
            for j in range(n, 0, -1):
                if A[i-1] == B[j-1]:
                    dp[j] = 1 + dp[j-1]
                    res = max(res, dp[j])
                else:
                    dp[j] = 0
        
        return res

    # my 1st trial, similar to find the max length of same subsequence using dynamic programming method
    # here the difference is the problem requires continuous subarray
    def findLength_Trial(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m, n = len(A), len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]

        res = 0
        for i in range(m+1):
            for j in range(n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res, dp[i][j])
        
        return res

A, B =  [1,2,3,2,1], [3,2,1,4,7]
print(Solution().findLength(A, B))