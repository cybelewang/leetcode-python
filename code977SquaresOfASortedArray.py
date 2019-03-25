"""
977 Squares of a Sorted Array

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""
class Solution:
    # my own solution with two pointers
    def sortedSquares(self, A):
        """
        :type A: list[int]
        :rtype: list[int]
        """
        squares = [0]*len(A)
        i, j = 0, len(A)-1
        for k in range(len(A)-1, -1, -1):
            i2, j2 = A[i]*A[i], A[j]*A[j]
            if i2 < j2:
                squares[k] = j2
                j -= 1
            else:
                squares[k] = i2
                i += 1

        return squares

#A = [1] # expect [1]
#A = [-1, 1] # expect [1, 1]
#A = [-1, 0, 1]  # expect [0, 1, 1]
A = [-7, -3, 1, 0, 2, 4, 5] # expect [0, 1, 4, 9, 16, 25, 49]
print(Solution().sortedSquares(A))