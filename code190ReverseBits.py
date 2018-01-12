"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = res*2 + n%2
            n //= 2
        return res

obj = Solution()
test_cases = [0, 2**32-1, 43261596]
for case in test_cases:
    print(case, end=' -> ')
    print(obj.reverseBits(case))