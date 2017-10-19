"""
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
        if not word1 and not word2:
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

test_cases = [(None, None), ('',''), ('', 'a'), ('a','a'), ('abcd', 'abd'), ('cd','abcd'), ('a', 'bac')]
obj = Solution()
for case in test_cases:
    print(case[0], end = '->')
    print(obj.minDistance(case[0],case[1]), end='->')
    print(case[1])
        
