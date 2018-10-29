"""
845 Longest Mountain in Array

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
"""
class Solution:
    # my own solution by observing the counts of increasing and decreasing segments
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0

        left, right, res = 0, 0, 0
        for i in range(1, n):
            if A[i] > A[i-1]:
                left += 1
                right = 0
            elif A[i] < A[i-1]:
                right += 1
                if left > 0:
                    res = max(res, left + right + 1)
            else:
                left = right = 0
        
        return res

#A = [2,1,4,7,3,2,5]
A = [5, 4, 3, 2, 1]
print(Solution().longestMountain(A))