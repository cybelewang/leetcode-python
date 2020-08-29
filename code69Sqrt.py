"""
69 Sqrt

Implement int sqrt(int x).

Compute and return the square root of x.

"""
# Ask cases: -1, not n^2
import unittest
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:   # Doesn't understand why we return x
            return x
        
        i, j, mid = 0, x, x//2
        while i <= j:
            mid = (i + j)//2
            pow2 = mid * mid
            if pow2 == x:
                return mid
            elif pow2 > x:
                j = mid - 1
            else:
                i = mid + 1
        
        return mid if mid**2 < x else mid - 1

# 2nd round solution on 7/3/2019
class Solution2(object):
    # binary search to find the upper_bound
    # the right boundary is x + 1
    def mySqrt(self, x):
        left, right = 0, x + 1 
        while left < right:
            mid = (left + right)//2
            if mid*mid <= x:
                left = mid + 1
            else:
                right = mid
        return right - 1

obj = Solution2()
class Test(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(obj.mySqrt(-1), -1)

    def test_zero(self):
        self.assertEqual(obj.mySqrt(0), 0)

    def test_positive(self):
        self.assertEqual(obj.mySqrt(1), 1)
        self.assertEqual(obj.mySqrt(8), 2)
        self.assertEqual(obj.mySqrt(4), 2)

if __name__ == '__main__':
    unittest.main(exit=False)

test_cases = [0, 1, 4, 9, 37, 144]
obj = Solution()
for case in test_cases:
    print(obj.mySqrt(case))