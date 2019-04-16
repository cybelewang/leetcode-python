"""
1023 Camelcase Matching

A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)
Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.

Example 1:
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: 
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".

Example 2:
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation: 
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".

Example 3:
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation: 
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".

Note:

1 <= queries.length <= 100
1 <= queries[i].length <= 100
1 <= pattern.length <= 100
All strings consists only of lower and upper case English letters.
"""
import re
class Solution:
    # regular expression solution
    def camelMatch_regex(self, qs, p):
        return [re.match("^[a-z]*" + "[a-z]*".join(p) + "[a-z]*$", q) != None for q in qs]

    # my own solution using two pointers
    # space O(1)
    # time O(Q*M*N), Q is the length of list queries, M is the average length of query, N is the length of pattern
    def camelMatch2(self, queries, pattern):
        def check(query, pattern):
            i, m = 0, len(query)
            for j in range(len(pattern)):
                # we should stop at any one of these (1) i reaches end of query, (2) query[i] is upper case letter, (3) query[i] == pattern[j]
                while i < m and query[i].islower() and query[i] != pattern[j]:
                    i += 1
                if i == m or query[i] != pattern[j]:
                    return False
                else:
                    i += 1

            return i == m or query[i:].islower()
        
        # main
        return [check(query, pattern) for query in queries]

    # my own solution, use DP to check each query and pattern
    # space O(M*N), M is the average length of query, N is the length of pattern
    # time O(Q*M*N), Q is the length of list queries
    def camelMatch(self, queries, pattern):
        """
        :type queries: list[str]
        :type pattern: str
        :rtype: list[bool]
        """
        def check(query, pattern):
            m, n = len(query), len(pattern)
            dp = [[False]*(n+1) for _ in range(m+1)]    # dp[i][j] means if query[:i] and pattern[:j] match
            dp[0][0] = True

            for i in range(1, m+1):
                for j in range(n+1):
                    dp[i][j] = (dp[i-1][j] and query[i-1].islower()) or \
                        (j > 0 and dp[i-1][j-1] and query[i-1] == pattern[j-1])
            
            return dp[m][n]
        
        # main
        return [check(query, pattern) for query in queries]

queries, pattern = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"
print(Solution().camelMatch_regex(queries, pattern))