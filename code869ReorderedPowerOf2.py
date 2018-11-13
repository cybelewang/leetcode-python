"""
869 Reordered Power of 2

Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.

Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
Example 4:

Input: 24
Output: false
Example 5:

Input: 46
Output: true
 

Note:

1 <= N <= 10^9
"""
class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        s = ''.join(sorted(str(N)))
        n = len(s)

        num = 1
        while len(str(num)) < n:
            num *= 2
        
        t = set()
        while len(str(num)) < n + 1:
            t.add(''.join(sorted(str(num))))
            num *= 2
        
        return s in t

test_N = [1, 2, 3, 4, 7, 8, 10, 16, 24, 46]
obj = Solution()
for N in test_N:
    print(N, end= '->')
    print(obj.reorderedPowerOf2(N))
