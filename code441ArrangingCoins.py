"""
441 Arranging Coins

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""
# (i+2)*(i+1) > 2*n
# i*(i+1) <= 2*n
from math import ceil
class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        n *= 2
        i = ceil(n**0.5)    # initialize i to the biggest possible value
        while i*(i+1) > n:  # decrease i until it meets the conditions
            i -= 1

        return i

obj = Solution()
print(obj.arrangeCoins(2**31-1))