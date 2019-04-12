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
# tag: number theory
class Solution:
    # https://leetcode.com/problems/smallest-integer-divisible-by-k/discuss/273080/Java-iterative
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K%2 == 0 or K%5 == 0:
            return -1

        i, count = 0, 0
        while i <= K:
            i = (i*10 + 1)%K
            count += 1

            if i == 0:
                return count
        
        return -1

test_K = [1, 2, 3, 5, 11, 17, 9999]
obj = Solution()
print(list(map(obj.smallestRepunitDivByK, test_K)))