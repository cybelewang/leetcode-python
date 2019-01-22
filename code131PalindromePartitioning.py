"""
131 Palindrome Partitioning

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

    # 2nd round solution on 12/20/2018, but has duplicated results
    # to avoid duplicated solutions, we must not partition s[:i], see the below 3rd round solution
    def partition2(self, s):
        n, res = len(s), []
        if s == s[::-1]:
            res.append([s])

        for i in range(1, n):
            for l in self.partition2(s[:i]):
                for r in self.partition2(s[i:]):
                    res.append(l + r)
        
        return res

    # 3rd round solution on 12/21/2018
    def partition3(self, s):
        res = []
        for i in range(1, len(s)):
            s1, s2 = s[:i], s[i:]
            if s1 == s1[::-1]:
                for right in self.partition3(s2):
                    res.append([s1] + right)

        if s == s[::-1]:
            res.append([s])

        return res

    # 1 line solution from https://leetcode.com/problems/palindrome-partitioning/discuss/42025/1-liner-Python-Ruby
    def partition4(self, s):
        return [[s[:i]] + rest
                for i in range(1, len(s)+1)
                if s[:i] == s[i-1::-1]
                for rest in self.partition4(s[i:])] or [[]]
        
obj = Solution()
test_case = 'aaaa'
print(obj.partition3(test_case))