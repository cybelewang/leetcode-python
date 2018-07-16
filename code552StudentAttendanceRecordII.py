"""
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 1e9 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
Note: The value of n won't exceed 100,000.
"""
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/6866756.html
    # Python TLE
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        M = 1000000007
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]

        for j in range(2):
            for k in range(3):
                dp[0][j][k] = 1
        
        for i in range(1, n+1):
            for j in range(2):
                for k in range(3):
                    val = dp[i-1][j][2]
                    if j > 0:
                        val = (val + dp[i-1][j-1][2]) % M
                    if k > 0:
                        val = (val + dp[i-1][j][k-1]) % M

                    dp[i][j][k] = val
                    
        return dp[n][1][2]

print(Solution().checkRecord(2))        