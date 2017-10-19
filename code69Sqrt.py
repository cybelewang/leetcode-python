"""
Implement int sqrt(int x).

Compute and return the square root of x.

"""
# Ask cases: -1, not n^2
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            raise ValueError
        
        i, j = 0, x
        while i <= j:
            mid = (i + j)//2
            pow2 = mid * mid
            if pow2 == x:
                return mid
            elif pow2 > x:
                j = mid - 1
            else:
                i = mid + 1
        
        # sqrt not found
        raise ValueError

test_cases = [0, 1, 4, 9, 144]
obj = Solution()
for case in test_cases:
    print(obj.mySqrt(case))