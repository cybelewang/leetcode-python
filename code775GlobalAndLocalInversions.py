"""
775 Global and Local Inversions

We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.
Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.
Note:

A will be a permutation of [0, 1, ..., A.length - 1].
A will have length in range [1, 5000].
The time limit for this problem has been reduced.
"""
class Solution:
    # http://www.cnblogs.com/grandyang/p/8983098.html
    def isIdealPermutation_OJBest(self, A):
        for i, num in enumerate(A):
            if abs(num - i) > 1:
                return False
        
        return True
        
    # my own solution, assume current number is A[i], then we need to check if there is a number in A[0, i-2] that is larger than A[i]
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n < 3:
            return True
        
        pre_max = A[0]
        for i in range(2, n):
            if pre_max > A[i]:
                return False
            pre_max = max(pre_max, A[i-1])

        return True

A = [0, 1, 4, 2, 3]
print(Solution().isIdealPermutation(A))