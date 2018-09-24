"""
650 2 Keys Keyboard

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Note:
The n will be in the range [1, 1000].
"""
class Solution:
"""
    #https://leetcode.com/problems/2-keys-keyboard/discuss/105897/Loop-best-case-log(n)-no-DP-no-extra-space-no-recursion-with-explanation
    public int minSteps(int n) {
        int s = 0;
        for (int d = 2; d <= n; d++) {
            while (n % d == 0) {
                s += d;
                n /= d;
            }
        }
        return s;
    } 
    """   
    # my own solution
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = list(range(n+1))
        dp[1] = 0

        for i in range(1, n+1):
            for j in range(2, n//i + 1):
                    dp[i*j] = min(dp[i*j], dp[i] + j)
        #print(dp)
        return dp[n]

print(Solution().minSteps(10))