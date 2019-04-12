"""
1015 Smallest Integer Divisible by K

Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.
Return the length of N.  If there is no such N, return -1.

Example 1:
Input: 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.

Example 2:
Input: 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.

Example 3:
Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.

Note:

1 <= K <= 10^5
"""
# 1. ask for length, not the integer
# 2. integer here has no 32-bit limit
class Solution:
    # my own solution
    # divide N to sum of 10^x, for example, 111 = 100 + 10 + 1. Then for each 10^x, module with K and add them to check if divisible by K
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K&1 == 0:
            return -1

        remain, factor, appeared = 0, 1, set()
        for i in range(1, 11):
            remain = (remain + factor%K)%K
            if remain == 0:
                return i
            else:
                factor *= 10
        
        return -1

test_K = [1, 2, 3, 5, 11, 9999]
obj = Solution()
print(list(map(obj.smallestRepunitDivByK, test_K)))