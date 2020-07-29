"""
805 Split Array With Same Average

In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)
Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.
Example :
Input: 
[1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
Note:
The length of A will be in the range [1, 30].
A[i] will be in the range of [0, 10000].
"""
class Solution:
    # https://www.cnblogs.com/grandyang/p/10285531.html
    def splitArraySameAverage(self, A):
        N = len(A)
        # dp[i] is a set with all sums of i numbers from A
        dp = [set() for _ in range(N//2+1)]
        dp[0].add(0) # 0 numbers result sum of 0
        for num in A:
            for i in range(N//2, 0, -1):
                for a in dp[i-1]:
                    dp[i].add(a + num)

        sums = sum(A)
        for i in range(1, N//2+1):
            if (i*sums%N) == 0 and (i*sums//N) in dp[i]:
                return True

        return False

A = [1, 2, 3, 4]
print(Solution().splitArraySameAverage(A))