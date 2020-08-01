"""
978 Longest Turbulent Subarray

A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.

Example 1:

Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:

Input: [4,8,12,16]
Output: 2
Example 3:

Input: [100]
Output: 1
 
Note:

1 <= A.length <= 40000
0 <= A[i] <= 10^9
"""
class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: list[int]
        :rtype: int
        """
        # encode "up" as 1, "down" as -1, "equal" as 0
        pre = A[0]
        A[0] = 0
        for i in range(1, len(A)):
            temp = A[i]
            if A[i] > pre:
                A[i] = 1
            elif A[i] < pre:
                A[i] = -1
            else:
                A[i] = 0
            pre = temp
        
        print(A)
        # we need to find the longest interlacing "1, -1, 1, -1, ...", or "-1, 1, -1, 1"
        i, res = 0, 1
        for j in range(1, len(A)):
            if A[j] == 0:
                i = j
            elif A[j] == A[j-1]:
                i = j - 1
            res = max(res, j - i + 1)

        return res

    def maxTurbulenceSize2(self, A):
        # relation: 1 for A[i-1] < A[i], -1 for A[i-1] > A[i], 0 for A[i-1] == A[i]
        # edges represent numbers of continuous turblent edges
        relation, edges, res = 0, 0, 1 

        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                if i == 1 or relation == -1:
                    edges += 1
                    res = max(res, edges+1)
                else:
                    edges = 1
                relation = 1
            elif A[i] < A[i-1]:
                if i == 1 or relation == 1:
                    edges += 1
                    res = max(res, edges+1)
                else:
                    edges = 1
                relation = -1
            else:
                relation, edges = 0, 0
                
        return res       

A = [1, 2, 1, 2, 1, 2]  # expect 6
#A = [0, 0, 0]   # expect 1
#A = [9,4,2,10,7,8,8,1,9]    # expect 5
print(Solution().maxTurbulenceSize(A))