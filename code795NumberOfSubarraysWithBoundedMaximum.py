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
        cnt0, block = 0, 0  # cnt0 is the count of numbers that are < L, block is the count of numbers which are all <= R
        res = 0
        for num in A:
            if num < L:
                cnt0 += 1
                block += 1
            elif num > R:
                res += block*(block + 1)//2 - cnt0*(cnt0 + 1)//2
                cnt0, block = 0, 0
            else:
                res -= cnt0*(cnt0+1)//2
                cnt0 = 0
                block += 1
        
        res += block*(block + 1)//2 - cnt0*(cnt0 + 1)//2

        return res

A, L, R = [2, 1, 4, 3], 2, 3    # expected 3
#A, L, R = [0, 2], 2, 3  # expected 2
#A, L, R = [0, 0, 0, 0], 2, 3 # expected 0
# A, L, R = [4, 4, 5, 6], 2, 3 # expected 0
#A, L, R = [0, 2, 0, 0, 2], 2, 3 # expected 11 
print(Solution().numSubarrayBoundedMax(A, L, R))