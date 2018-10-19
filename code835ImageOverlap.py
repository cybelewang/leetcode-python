"""
835 Image Overlap

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  
After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes: 

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
"""
import collections
class Solution:
    # help from https://blog.csdn.net/zjucor/article/details/80298134
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        N = len(A)
        LA = [(i, j) for i in range(N) for j in range(N) if A[i][j]]
        LB = [(i, j) for i in range(N) for j in range(N) if B[i][j]]
        c = collections.Counter((x1 - x2, y1 - y2) for x1, y1 in LA for x2, y2 in LB)
        return max(c.values() or [0])

A = [[1,1,0],
    [0,1,0],
    [0,1,0]]

B = [[0,0,0],
    [0,1,1],
    [0,0,1]]

print(Solution().largestOverlap(A, B))