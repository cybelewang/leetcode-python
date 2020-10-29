"""
896 Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
 

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        pos, neg = 0, 0
        for i in range(1, n):
            if A[i] - A[i-1] > 0:
                pos += 1
            elif A[i] - A[i-1] < 0:
                neg += 1
        
        return pos*neg == 0 # at least one of them must be 0

    # https://leetcode.com/problems/monotonic-array/solution/
    def isMonotonic2(self, A):
        increase = decrease = False
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                increase = True
            elif A[i] < A[i-1]:
                decrease = True
        
        return not (increase and decrease)

A = [1, 1, 1]
print(Solution().isMonotonic(A))