"""
941 Valid Mountain Array

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
 

Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000 
"""
class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n < 3:
            return False

        i, j = 0, n-1
        # search from left to right
        while i+1 < n and A[i] < A[i+1]:
            i += 1
        # search from right to left
        while j-1 > 0 and A[j] < A[j-1]:
            j -= 1
        
        # i and j must meet at some place between 0 and n-1
        return i==j and 0 < i < n-1

A = [0, 3, 2, 1]
print(Solution().validMountainArray(A))
