"""
821 Shortest Distance to a Character

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""
class Solution:
    # my own two-pass solution
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        dist, last = [n]*n, -n
        for i in range(n):
            if S[i] == C:
                last = i
            dist[i] = min(dist[i], i-last)

        last = -n
        for i in range(n-1, -1, -1):
            if S[i] == C:
                last = i
            dist[i] = min(dist[i], last - i)
        
        return dist

S = "loveleetcode"
C = 'e'
print(Solution().shortestToChar(S, C))