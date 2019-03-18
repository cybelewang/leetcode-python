"""
961 N-Repeated Element in Size 2N Array

In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
"""
class Solution:
    # Moore majority algorithm
    def repeatedNTimes(self, A):
        """
        A: list[int]
        rtype: int
        """
        cnt, e = 0, 0
        for a in A:
            if cnt == 0:
                cnt, e = 1, a
            elif a == e:
                cnt += 1
            else:
                cnt -= 1
        
        return e

A = [5,5,5,5,1,2,3,4]
print(Solution().repeatedNTimes(A))
        