"""
879 Profitable Schemes

There is a group of G members, and a list of various crimes they could commit.

The ith crime generates a profit[i] and requires group[i] members to participate in it.

If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least P profit, and the total number of members participating in that subset of crimes is at most G.

How many schemes can be chosen?  Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:

Input: G = 5, P = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: 
To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
Example 2:

Input: G = 10, P = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: 
To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
 
Note:

1 <= G <= 100
0 <= P <= 100
1 <= group[i] <= 100
0 <= profit[i] <= 100
1 <= group.length = profit.length <= 100
"""
class Solution:
    # DP solution
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        M = 10**9 + 7
        dp = [[0]*(G+1) for _ in range(P+1)] # dp[i][j] are schemes of i profit and j people
        dp[0][0] = 1
        for g, p in zip(group, profit):
            for i in range(P, -1, -1):
                for j in range(G-g, -1, -1):
                    dp[min(i+p, P)][j+g] = (dp[min(i+p, P)][j+g] + dp[i][j]) % M
        
        return sum(dp[P]) % M    

    # DFS + Cache, TLE
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        n, M = len(group), 10**9 + 7
        # number of schemes for given people g, profit p, and start index of group/profit
        def helper(g, p, start, mem):
            if g > G: return 0
            if (g, p, start) in mem: return mem[(g, p, start)]
            ans = 0
            if p >= P: ans = 1
            for i in range(start, n):
                ans = (ans + helper(g + group[i], p + profit[i], i+1, mem)) % M
            mem[(g, p, start)] = ans
            return ans
        
        return helper(0, 0, 0, {})