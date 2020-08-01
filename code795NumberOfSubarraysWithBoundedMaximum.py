"""
795 Number of Subarrays with Bounded Maximum

We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

Example :
Input: 
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Note:

L, R  and A[i] will be an integer in the range [0, 10^9].
The length of A will be in the range of [1, 50000].
"""
import unittest
class Solution:
    # my own O(n)-time solution
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        # we use 0 to represent numbers < L, 1 to represent numbers between L and R, 2 to represent numbers > R
        # continuous subarrays with all elements < L, should be excluded
        # continuous subarrays with any element > R, should be excluded
        cntL, cntR = 0, 0  # cntL is the count of numbers that are < L, cntR is the count of numbers which are all <= R
        res = 0
        for num in A:
            if num < L:
                cntL += 1
                cntR += 1
            elif num > R:
                res += cntR*(cntR + 1)//2 - cntL*(cntL + 1)//2
                cntL, cntR = 0, 0
            else:
                res -= cntL*(cntL+1)//2
                cntL = 0
                cntR += 1
        
        res += cntR*(cntR + 1)//2 - cntL*(cntL + 1)//2

        return res

    # https://www.cnblogs.com/grandyang/p/9237967.html
    # Improved from the count(A, R) - count(A, L-1) so we can solve it in one pass.
    # cntL is the count of continuous numbers < L
    # cntR is the count of continuous numbers <=R
    # for each number a, update cntL and cntR accordingly, and at the end, add cntR-cntL
    def numSubarrayBoundedMax2(self, A, L, R):
        cntL, cntR = 0, 0
        res = 0
        for a in A:
            if a < L: 
                cntL += 1
                cntR += 1
            elif a <=R:
                cntL = 0
                cntR += 1
            else:
                cntL = cntR = 0
            
            res += cntR - cntL
            
        return res

    # two pass solution
    def numSubarrayBoundedMax3(self, A, L, R):
        def count(A, b):
            cur, res = 0, 0
            for a in A:
                if a <= b: cur += 1
                else: cur = 0
                res += cur
            
            return res
        
        return count(A, R) - count(A, L-1)

class Test(unittest.TestCase):
    def test_1(self):
        obj = Solution()
        A, L, R = [2, 1, 4, 3], 2, 3
        self.assertEqual(obj.numSubarrayBoundedMax3(A, L, R), 3)
        A, L, R = [0, 2], 2, 3
        self.assertEqual(obj.numSubarrayBoundedMax3(A, L, R), 2)
        A, L, R = [0, 0, 0, 0], 2, 3
        self.assertEqual(obj.numSubarrayBoundedMax3(A, L, R), 0)
        A, L, R = [4, 4, 5, 6], 2, 3
        self.assertEqual(obj.numSubarrayBoundedMax3(A, L, R), 0)
        A, L, R = [0, 2, 0, 0, 2], 2, 3
        self.assertEqual(obj.numSubarrayBoundedMax3(A, L, R), 11)
        A, L, R = [73,55,36,5,55,14,9,7,72,52], 32, 69
        self.assertEqual(obj.numSubarrayBoundedMax3(A, L, R), 22)
        
if __name__ == "__main__":
    unittest.main(exit = False)