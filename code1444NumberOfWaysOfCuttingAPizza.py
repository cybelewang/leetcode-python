"""
1444 Number of Ways of Cutting a Pizza

Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

Example 1:
Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.

Example 2:
Input: pizza = ["A..","AA.","..."], k = 3
Output: 1

Example 3:
Input: pizza = ["A..","A..","..."], k = 1
Output: 1

Constraints:
1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
"""
class Solution:
    # https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/discuss/623732/JavaC%2B%2BPython-DP-%2B-PrefixSum-in-Matrix-Clean-code
    # prefix Sum + DP
    # Since we will cut and give either top or left part, the bottom right cell is always kept, so we use preSum(r, c) to represent the number of apples from cell (r, c) to (m-1, n-1)
    # Then for each cell (r, c), we will try to iterate all below rows (nr, c), as long as there are apples between (r, c) and (nr, c), we can cut and give top, then recursively call dp(nr, c, k-1)
    # Also we can iterate all left columns (r, nc), as long as there are apples between (r, nc) and (r, c), we can cut and give left, then recursively call dp(r, nc, k-1)
    def ways(self, pizza: List[str], k: int) -> int:
        m, n, MOD = len(pizza), len(pizza[0]), 10**9+7
        preSum = [[0]*(n+1) for _ in range(m+1)]
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                preSum[r][c] = preSum[r+1][c] + preSum[r][c+1] - preSum[r+1][c+1] + (1 if pizza[r][c] == 'A' else 0)
        
        @lru_cache(None)
        def dp(r, c, k):
            if preSum[r][c] == 0:
                return 0
            if k == 1:
                return 1
            ans = 0
            for nr in range(r+1, m):
                if preSum[r][c] - preSum[nr][c] > 0:
                    ans = (ans + dp(nr, c, k-1)) % MOD
            
            for nc in range(c+1, n):
                if preSum[r][c] - preSum[r][nc] > 0:
                    ans = (ans + dp(r, nc, k-1)) % MOD
                    
            return ans
        
        return dp(0, 0, k)

    # backtracking, TLE
    # count apples on each row and each column
    def ways(self, pizza: List[str], k: int) -> int:
        if k == 1:
            return int(any(row.count('A') > 0 for row in pizza))
        
        m, n = len(pizza), len(pizza[0])
        rows, cols = [0]*m, [0]*n
        for i in range(m):
            for j in range(n):
                if pizza[i][j] == 'A':
                    rows[i] |= 1
                    cols[j] |= 1
        
        rowCnt = [0]
        for i in range(m):
            rowCnt.append(rowCnt[-1] + rows[i])
        
        colCnt = [0]
        for j in range(n):
            colCnt.append(colCnt[-1] + cols[j])
        
        res = 0
        for i in range(1, m):
            if rowCnt[i] > 0:
                res += self.ways(pizza[i:], k-1)
        
        for j in range(1, n):
            if colCnt[j] > 0:
                new_pizza = [row[j:] for row in pizza]
                res += self.ways(new_pizza, k-1)
        
        res %= 10**9 + 7
        return res