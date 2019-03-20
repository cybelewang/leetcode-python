"""
967 Numbers With Same Consecutive Differences

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.
Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.
You may return the answer in any order.

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Note:

1 <= N <= 9
0 <= K <= 9
"""
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        def num(build):
            ans, factor = 0, 1
            for i in range(len(build)-1, -1, -1):
                ans += factor*build[i]
                factor *= 10

            return ans

        def dfs(build, K, remain, res):
            if remain == 0:
                res.append(num(build))
                return
            last = build[-1]
            if last + K < 10:
                build.append(last + K)
                dfs(build, K, remain - 1, res)
                build.pop()
            if K != 0 and last - K > -1:
                build.append(last - K)
                dfs(build, K, remain-1, res)            
                build.pop()

        # main
        build, res = [], []
        for x in range(1, 10):
            build.append(x)
            dfs(build, K, N-1, res)
            build.pop()
        
        return res

print(Solution().numsSameConsecDiff(2, 1))