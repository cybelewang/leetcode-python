"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
"""
# http://www.cnblogs.com/grandyang/p/5411919.html
# what's the math behind this algorithm? https://leetcode.com/problems/integer-break/discuss/80721/Why-factor-2-or-3-The-math-behind-this-problem.
class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        res = [1, 1, 1, 2, 4, 6, 9]
        if n < 7:
            return res[n]

        for i in range(7, n+1):
            res.append(3*res[i-3])

        return res[-1]

obj = Solution()
print(obj.integerBreak(10))