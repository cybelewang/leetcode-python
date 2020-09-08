"""
72 Edit Distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 is None or word2 is None:
            return 0

        m = len(word1)
        n = len(word2)

        dist = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(1, m+1):
            dist[i][0] = i  # delete i characters to achieve an empty string

        for j in range(1, n+1):
            dist[0][j] = j # insert i characters to achieve a string with length j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                replace = dist[i-1][j-1] if word1[i-1] == word2[j-1] else dist[i-1][j-1] + 1
                delete = dist[i-1][j] + 1
                insert = dist[i][j-1] + 1
                dist[i][j] = min(replace, delete, insert)
        
        return dist[m][n]

# 2nd round solution on 9/19/2018
class Solution2:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for j in range(1, n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            dp[i][0] = i
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] + 1

                dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)    # insert a character to word1's end
                dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)    # delete a character from word2's end
        
        return dp[m][n]

    # 1D DP solution
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n+1))        
        for i in range(1, m+1):
            pre = dp[0]
            dp[0] = i
            for j in range(1, n+1):
                temp = dp[j]
                dp[j] = min(dp[j] + 1, dp[j-1] + 1)
                if word1[i-1] == word2[j-1]:
                    dp[j] = min(dp[j], pre)
                else:
                    dp[j] = min(dp[j], pre+1)
                pre = temp
                    
        return dp[n]

test_cases = [('',''), ('', 'a'), ('a','a'), ('abcd', 'abd'), ('cd','abcd'), ('a', 'bac')]
obj = Solution()
for case in test_cases:
    print(case[0], end = '->')
    print(obj.minDistance(case[0],case[1]), end='->')
    print(case[1])
        
