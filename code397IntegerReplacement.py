"""
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
"""
class Solution:
    # http://bookshadow.com/weblog/2016/09/11/leetcode-integer-replacement/
    # if n is even, n //= 2
    # if n is odd, check the lowest 2 bits: for '01', n -= 1 to acheive '00'; for '11', n += 1 to achieve '00', the purpose is to reduce number of '1' in n
    # 3 is an exception
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n != 1:
            if n & 1 == 0:
                n //= 2
            elif n == 3 or ((n//2) & 1 == 0):
                n -= 1
            else:
                n += 1
            res += 1
        
        return res

    # recursive solution, since the depth is about log2(n), not very large
    def integerReplacement2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        if n & 1 == 0: return self.integerReplacement2(n//2) + 1
        return min(self.integerReplacement2(n+1), self.integerReplacement2(n-1)) + 1

    # my own DP solution, overflow error for very large n, such as 2**31-1
    def integerReplacement3(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0

        dp = [0]*(n+1)
        dp[1] = 0

        for i in range(2, n+1):
            if i % 2 == 0:
                # i is even
                dp[i] = dp[i//2] + 1
            else:
                # i is odd
                dp[i] = min(dp[(i-1)//2], dp[(i+1)//2]) + 2
        
        return dp[n]

obj = Solution()
test_cases = [1, 2, 3, 4, 7, 8, 100, 2**31-1]
for case in test_cases:
    print(case, end=' -> ')
    print(obj.integerReplacement2(case))