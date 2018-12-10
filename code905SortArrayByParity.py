"""
905 Sort Array By Parity

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""
# on-site interview question of G
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] & 1 == 0:   # A[i] is even
                i += 1
            elif A[j] & 1 != 0: # A[j] is odd
                j -= 1
            else:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        
        return A

A = [3,1,2,4]
print(Solution().sortArrayByParity(A))