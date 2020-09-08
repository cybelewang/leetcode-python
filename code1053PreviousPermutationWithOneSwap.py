"""
1053 Previous Permutation With One Swap

Given an array A of positive integers (not necessarily distinct), return the lexicographically largest permutation that is smaller than A, that can be made with one swap (A swap exchanges the positions of two numbers A[i] and A[j]).  If it cannot be done, then return the same array.

Example 1:

Input: [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.
Example 2:

Input: [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.
Example 3:

Input: [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
Example 4:

Input: [3,1,1,3]
Output: [1,3,1,3]
Explanation: Swapping 1 and 3.

Note:

1 <= A.length <= 10000
1 <= A[i] <= 10000
"""
class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)
        # from right to left, find the first pair that A[i] > A[i+1]
        i = n - 2
        while i > -1 and A[i] <= A[i+1]:
            i -= 1
        # A is in non-ascending order from right to left, no previous permutation available
        if i == -1: return A

        # now A[i] > A[i+1]
        # from left to right, find the first A[j] < A[i]
        j = i + 1
        while j < n and A[j] < A[i]:
            j += 1        
        j -= 1

        # now from right to left, find the most left one with same value as A[j]
        # in case that there are multiple A[j], the most left one will generate the largest permutation that < A
        while j > i and A[j-1] == A[j]:
            j -= 1
            
        A[i], A[j] = A[j], A[i]
        return A