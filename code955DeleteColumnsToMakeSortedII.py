"""
955 Delete Columns to Make Sorted II

We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef","vyz"].

Suppose we chose a set of deletion indices D such that after deletions, the final array has its elements in lexicographic order (A[0] <= A[1] <= A[2] ... <= A[A.length - 1]).

Return the minimum possible value of D.length.

Example 1:

Input: ["ca","bb","ac"]
Output: 1
Explanation: 
After deleting the first column, A = ["a", "b", "c"].
Now A is in lexicographic order (ie. A[0] <= A[1] <= A[2]).
We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.
Example 2:

Input: ["xc","yb","za"]
Output: 0
Explanation: 
A is already in lexicographic order, so we don't need to delete anything.
Note that the rows of A are not necessarily in lexicographic order:
ie. it is NOT necessarily true that (A[0][0] <= A[0][1] <= ...)
Example 3:

Input: ["zyx","wvu","tsr"]
Output: 3
Explanation: 
We have to delete every column.

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
"""
class Solution:
    def minDeletionSize(self, A):
        ignore = [False]*len(A) # ignore[i] is "do we need to check Col[i] <= Col[i+1]"
        

    # O(N*W^2) time, add a column letter each time and check if they are sorted
    def minDeletionSize2(self, A):
        def is_sorted(A):
            return all(A[i] <= A[i+1] for i in range(len(A) - 1))
        
        cur = [""]*len(A)
        res = 0
        for col in zip(*A):
            cur2 = cur[:]
            for i, letter in enumerate(col):
                cur2[i] += letter
            if is_sorted(cur2):
                cur = cur2
            else:
                res += 1
        
        return res
    
    # wrong solution on A = ["xga","xfb","yfa"]
    def minDeletionSize_WRONG(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        n, m, res = len(A), len(A[0]), 0
        for j in range(m):
            large, small = 0, 0
            for i in range(1, n):
                if A[i][j] > A[i-1][j]:
                    large += 1
                elif A[i][j] < A[i-1][j]:
                    small += 1

            if small > 0:
                res += 1
            elif large > 0:
                return res
        
        return res

A = ["xga","xfb","yfa"]
#A = ["xc","yb","za"]
print(Solution().minDeletionSize(A))