"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""
# DP + DFS
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        if n < 2:
            return [[s]]
        
        # Get the palindrome matrix, see problem 5, longest palindromic substring
        P = [[True for j in range(n)] for i in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                P[i][j] = P[i+1][j-1] and (s[i] == s[j])
        
        res = []
        self._dfs(s, 0, P, [], res)

        return res

    def _dfs(self, s, start, P, build, res):
        """
        start: start index of next candidate string
        P: the palindrome matrix
        build: the candidate list of palindrome substrings
        res: the result list
        """
        n = len(s)
        if start == n:
            res.append(build[:])
            return

        for end in range(start, n):
            if P[start][end]:
                build.append(s[start:end+1])
                self._dfs(s, end+1, P, build, res)
                build.pop()
        
obj = Solution()
test_case = ''
print(obj.partition(test_case))