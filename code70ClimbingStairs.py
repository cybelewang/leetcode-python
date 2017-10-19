"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1

        below2, below1 = 1, 1
        cur = 2

        for i in range(2, n+1): # bug fixed: should use n+1, not n
            cur = below2 + below1
            below2 = below1
            below1 = cur
        
        return cur

obj = Solution()
for test_num in range(2, 11):
    print(test_num, end = ' -> ')
    print(obj.climbStairs(test_num))
