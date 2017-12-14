"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
class Solution:
    
    # The best solution is not using DP to get the palindrome matrix, but iterate all centers of substrings then check if the substring is palindrome
    # time O(n^2), space O(n)
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return 0

        minCuts = [l - 1 for l in range(n+1)]   # number of cuts for substring s[0:i] with lenth l, initialized with worst case

        for i in range(n):  # iterate all center letters
            
            # odd length substring with s[i] as center letter
            j = 0
            while j <= i and i + j < n and s[i-j] == s[i+j]:                
                minCuts[i+j+1] = min(minCuts[i+j+1], 1 + minCuts[i-j])
                j += 1
            
            # even length substring with s[i] as last letter in left half
            j = 1
            while j <= i+1 and i + j < n and s[i-j+1]==s[i+j]:                
                minCuts[i+j+1] = min(minCuts[i+j+1], 1 + minCuts[i-j+1])
                j += 1
        
        return minCuts[n]


    # 2nd try, DP, time O(n^2), space O(n^2), http://fisherlei.blogspot.com/2013/03/leetcode-palindrome-partitioning-ii.html
    def minCut2(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return 0

        minCuts = [n - i - 1 for i in range(n+1)]   # minCuts[i] represents the min cuts for substring s[i:]. Initialize this list with worst case cuts

        # Get the palindrome matrix, see problem 5, longest palindromic substring
        P = [[True for j in range(n)] for i in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                P[i][j] = P[i+1][j-1] and (s[i] == s[j])
                if P[i][j]:
                    minCuts[i] = min(minCuts[i], 1 + minCuts[j+1])  # here "1" represents the cut to separate string s[i, j] and s[j+1, n-1], we can cut here because s[i, j] is palindromic
        
        return minCuts[0]
        
    # 1st try, DP + BFS, got TLE
    def minCut3(self, s):
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
test_cases = ['','a','ab','aaaa','aba','abda']
for case in test_cases:
    print(case + ' -> ', end='')
    print(obj.minCut(case))