"""
552 Student Attendance Record II

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
    # solution 3 from http://www.cnblogs.com/grandyang/p/6866756.html
    # key idea is to consider rewardable strings without 'A' first, then replace each letter in rewardable strings with 'A'
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        M = 1000000007
        P = [0]*(n+1)   # P[i] is number of length i rewardable strings ending with "P"
        PorL = [0]*(n+1)    # PorL[i] is number of length i rewardable strings ending with "P" or "L"
        P[0] = 1
        PorL[0] = 1
        PorL[1] = 2

        for i in range(1, n+1):
            P[i] = PorL[i-1]
            if i > 1:
                PorL[i] = (P[i] + P[i-1] + P[i-2]) % M  # P[i-1] + P[i-2] is for strings ending with 'L' (or L[i]), because L can be appended to P (P[i-1]), or to L but L's previous letter is P (P[i-2] = PorL[i-2] - L[i-2])

        res = PorL[n]
        for i in range(n):
            # replace [i] in rewardable strings (without A) with 'A'
            t = (PorL[i] * PorL[n-1-i]) % M # left and right sides are independent
            res = (res + t) % M
        
        return res

    # solution 2 from http://www.cnblogs.com/grandyang/p/6866756.html
    # P[i], L[i], A[i] represents number of rewardable strings 0:i (inclusive), ending with 'P', 'L', 'A' respectively
    def checkRecord2(self, n):
        """
        :type n: int
        :rtype: int
        """
        M = 1000000007
        P, L, A = [0]*n, [0]*n, [0]*n

        P[0] = 1
        L[0] = 1
        L[1] = 3
        A[0] = 1
        A[1] = 2
        A[2] = 4

        for i in range(1, n):
            P[i] = (P[i-1] + L[i-1])% M + A[i-1] % M    # P can be appended to any letter
            if i > 1:
                L[i] = ((A[i - 1] + P[i - 1]) % M + (A[i - 2] + P[i - 2]) % M) % M  # L can be appended to P, A. if L appends to L, we need to check if previous L's previous letter is L too. With exclusive method, we can figure out total[i-2] - L[i-2] = P[i-2] + L[i-2]
            if i > 2:
                A[i] = ((A[i - 1] + A[i - 2]) % M + A[i - 3]) % M   # see explanation from http://www.cnblogs.com/grandyang/p/6866756.html
        
        return ((A[n - 1] + P[n - 1]) % M + L[n - 1]) % M

    # don't understand solution 1 from http://www.cnblogs.com/grandyang/p/6866756.html
    # Python TLE
    def checkRecord3(self, n):
        """
        :type n: int
        :rtype: int
        """
        M = 1000000007
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]

        for j in range(2):
            for k in range(3):
                dp[0][j][k] = 1 # there is always a 0-length record, empty string ''
        
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

print(Solution().checkRecord(5))        