"""
351 Android Unlock Patterns
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.
 
Explanation:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
 

Invalid move: 4 - 1 - 3 - 6 
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

Example:
Given m = 1, n = 1, return 9.
"""
class Solution:
    def numberOfPatterns(self, m, n):
        res, visited = 0, [False]*10
        jumps = [[0]*10 for _ in range(10)] # 10x10 matrix with jumps[i][j] is the number between i and j, if there is no number between i and j, the value will be 0

        # initialize jumps
        jumps[1][3] = jumps[3][1] = 2
        jumps[4][6] = jumps[6][4] = 5
        jumps[7][9] = jumps[9][7] = 5
        jumps[1][7] = jumps[7][1] = 4
        jumps[2][8] = jumps[8][2] = 5
        jumps[3][9] = jumps[9][3] = 6
        jumps[1][9] = jumps[9][1] = jumps[3][7] = jumps[7][3] = 5

        res += self.helper(1, 1, 0, m, n, jumps, visited) * 4   # 1, 3, 7, 9 are symmetric
        res += self.helper(2, 1, 0, m, n, jumps, visited) * 4   # 2, 4, 6, 8 are symmetric
        res += self.helper(5, 1, 0, m, n, jumps, visited)

        return res
    
    def helper(self, num, length, count, m, n, jumps, visited):
        '''
        num: current start number
        length: current length of keys in pattern
        count: current count of valid path
        '''
        if length >= m:
            count += 1
        length += 1
        if length > n:
            return count
        
        visited[num] = True
        for next in range(1, 10):
            jump = jumps[num][next]
            if not visited[next] and (jump == 0 or visited[jump]):
                self.helper(next, length, count, m, n, jumps, visited)
        
        visited[num] = False
        return count

print(Solution().numberOfPatterns(1, 1))