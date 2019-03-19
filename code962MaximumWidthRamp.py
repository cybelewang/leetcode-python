"""
962 Maximum Width Ramp

Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation: 
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: 
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.

Note:

2 <= A.length <= 50000
0 <= A[i] <= 50000
 """
class Solution:
    # my own solution
    def maxWidthRamp(self, A):
        # binary search on a decreasing index array (A[down_index[i]] > A[down_index[i+1]])
        # find and return the smallest index i such that A[down_index[i]] <= x
        # if the result i == len(down_index), this means there is no such i
        def search(A, down_index, x):
            i, j = 0, len(down_index)
            while i < j:
                mid = (i + j)//2
                if A[down_index[mid]] > x:
                    i = mid + 1
                else:
                    j = mid
            
            return i

        down_index, res = [], 0
        for j, a in enumerate(A):
            i = search(A, down_index, a)
            if i < len(down_index):
                res = max(res, j - down_index[i])
            if not down_index or A[down_index[-1]] > a:
                down_index.append(j)

        return res        

#A = [9,8,1,0,1,9,4,0,4,1]  # expect 7
#A = [6,0,8,2,1,5]   # expect 4
#A = [4,3,2,1] # expect 0
#A = [2,2,2,2]   # expect 3
A = [5, 5, 6, 7, 3, 2, 1, 0, 4] # expect 4 (3 to 4)
print(Solution().maxWidthRamp(A))            