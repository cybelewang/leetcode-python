"""
976 Largest Perimeter Triangle

Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.
If it is impossible to form any triangle of non-zero area, return 0.

Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8

Note:

3 <= A.length <= 10000
1 <= A[i] <= 10^6
"""
import itertools
class Solution:
    # O(NlogN)
    # first sort A
    # reversely iterate A, and select three consequent lengths A[i-2], A[i-1], A[i] as a, b, c
    # we already know that a <= b <= c, so abs(a-b) < c
    # next we need to check if a + b > c, if this condition is met, we get the largest perimeter. Why?
    # The reason is even there exists smaller i, which also meets aa + bb > cc, they must obey aa < a, bb <= b, cc <= c, so their sum must be smaller
    def largestPerimeter(self, A):
        A.sort()
        res = 0
        for i in range(len(A)-1, 1, -1):
            if A[i-2] + A[i-1] > A[i]:
                res = A[i-2] + A[i-1] + A[i]
                break
        
        return res
        
    # brutal force solution
    # O(N^3)
    def largestPerimeter2(self, A):
        """
        :type A: list[int]
        :rtype: int
        """
        res = 0
        for a, b, c in itertools.combinations(A, 3):
            if (a + b > c) and (abs(a-b) < c):
                res = max(res, a + b + c)
        
        return res

A = [3,6,2,3]
print(Solution().largestPerimeter(A))