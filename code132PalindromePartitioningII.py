"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
    # DP + BFS, got TLE
    def minCut2(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return 0

        # Get the palindrome matrix, see problem 5, longest palindromic substring
        P = [[True for j in range(n)] for i in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                P[i][j] = P[i+1][j-1] and (s[i] == s[j])
        
        # BFS to find the minimum cuts
        cuts = 0
        queue = [0] # start index of next palindrome substring

        while len(queue) > 0:
            next_queue = []
            for i in queue:
                for j in range(i, n):
                    if P[i][j]:
                        if j == n-1:
                            return cuts
                        else:
                            next_queue.append(j+1)
            
            queue = next_queue
            cuts += 1
        
        return cuts # ideally this return statement should not be called, instead the function will return inside the while loop

obj = Solution()
test_case = 'aaaac'
print(obj.minCut2(test_case))