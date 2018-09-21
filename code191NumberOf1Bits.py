"""
191 Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            res += n%2
            n //= 2
        
        return res

obj = Solution()
test_cases = [0, 2**32-1, 11]
for case in test_cases:
    print(case, end=' -> ')
    print(obj.hammingWeight(case))