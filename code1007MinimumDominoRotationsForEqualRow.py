"""
1007 Minimum Domino Rotations For Equal Row

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
We may rotate the i-th domino, so that A[i] and B[i] swap values.
Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Example 1:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.

Note:

1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000
"""
class Solution:
    # Find intersection set s of {A[i], B[i]}
    # s.size = 0, no possible result.
    # s.size = 1, one and only one result.
    # s.size = 2, it means all dominoes are [a,b] or [b,a], try either one.
    # s.size > 2, impossible.
    def minDominoRotations_OJ(self, A, B):
        s = reduce(set.__and__, [set(d) for d in zip(A, B)])
        if not s: return -1
        x = s.pop()
        return min(len(A) - A.count(x), len(B) - B.count(x))
    # my own solution
    # count each number (1 to 6)'s appearance on top, on bottom and on both
    # then go through each number and calculate the min rotations
    def minDominoRotations(self, A, B):
        """
        :type A: list[int]
        :type B: list[int]
        :rtype: int
        """
        N = len(A)
        top, bottom, both = [0]*7, [0]*7, [0]*7
        for i in range(N):
            top[A[i]] += 1
            bottom[B[i]] += 1
            if A[i] == B[i]:
                both[A[i]] += 1
        
        res = 20001
        for i in range(1, 7):
            if top[i] + bottom[i] - both[i] >= N:
                res = min(res, N - max(top[i], bottom[i]))    # bug fixed: previously was N - both[i] - max(top[i], bottom[i])
        
        return -1 if res == 20001 else res

#A, B = [1, 1], [2, 2]   # expect 0
#A, B = [1, 2, 1], [1, 1, 3] # expect 1
#A, B = [1, 1, 3], [1, 2, 2] # expect -1
A, B = [1, 1, 1, 1, 2, 2, 2], [2, 2, 2, 2, 1, 1, 1] # expect 3
print(Solution().minDominoRotations(A, B))