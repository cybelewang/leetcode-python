"""
629 K Inverse Pairs Array

Given two integers n and k, find how many different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs.

We define an inverse pair as following: For ith and jth element in the array, if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.

Since the answer may be very large, the answer should be modulo 10^9 + 7.

Example 1:
Input: n = 3, k = 0
Output: 1
Explanation: 
Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.
Example 2:
Input: n = 3, k = 1
Output: 2
Explanation: 
The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
Note:
The integer n is in the range [1, 1000] and k is in the range [0, 1000].
"""
class Solution:
    # Solution 2 from http://www.cnblogs.com/grandyang/p/7111385.html
    # also see https://leetcode.com/problems/k-inverse-pairs-array/discuss/104815/Java-DP-O(nk)-solution
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        M = 1000000007
        dp = [[0]*(k+1) for _ in range(n+1)]    # dp[i][j] is the number of arrays (1 to i) which has j inverse pairs
        dp[0][0] = 1

        for i in range(1, n+1):
            dp[i][0] = 1
            for j in range(1, k+1):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%M
                if j >= i:
                    dp[i][j] = (dp[i][j] - dp[i-1][j-i] + M)%M
        print(dp)
        return dp[n][k]

    # Solution 1 from http://www.cnblogs.com/grandyang/p/7111385.html
    def kInversePairs2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        M = 1000000007
        dp = [[0]*(k+1) for _ in range(n+1)]    # dp[i][j] is the number of arrays (1 to i) which has j inverse pairs
        dp[0][0] = 1

        for i in range(n+1):
            for j in range(i):
                for m in range(k+1):
                    if m - j > -1 and m - j <= k:
                        dp[i][m] = (dp[i][m] + dp[i-1][m-j])%M
        print(dp)
        return dp[n][k]

    # my 1st trial using DP, TLE
    # dp[i][j] is the number of arrays (1 to i) which has j inverse pairs
    # dp[i][j] can be get by putting i into position m for array with numbers from 1 to i, so (i-m) numbers will be moved to right and caused (i-m) more inverse pairs
    def kInversePairs3(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        M = 1000000007
        dp = [[0]*(k+1) for _ in range(n+1)]    # dp[i][j] is the number of arrays (1 to i) which has j inverse pairs
        dp[0][0] = 1
        for i in range(1, n+1):
            dp[i][0] = 1
            for j in range(1, k+1):
                for p in range(j, max(j-i+1, 0)-1, -1):
                    dp[i][j] = (dp[i][j] + dp[i-1][p])%M
        print(dp)
        return dp[n][k]

print(Solution().kInversePairs3(3, 2))
