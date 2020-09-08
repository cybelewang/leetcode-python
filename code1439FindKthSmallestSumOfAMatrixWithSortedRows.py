"""
1439 Find the Kth Smallest Sum of a Matrix With Sorted Rows

You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.

You are allowed to choose exactly 1 element from each row to form an array. Return the Kth smallest array sum among all possible arrays.

Example 1:

Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.  
Example 2:

Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17
Example 3:

Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  
Example 4:

Input: mat = [[1,1,10],[2,2,9]], k = 7
Output: 12

Constraints:
m == mat.length
n == mat.length[i]
1 <= m, n <= 40
1 <= k <= min(200, n ^ m)
1 <= mat[i][j] <= 5000
mat[i] is a non decreasing array.
"""
from heapq import heapify, heappush, heappop
class Solution:
    # divide and conquer method
    # merge every row and update the result
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        res = [mat[0][j] for j in range(min(n, k))]
        for i in range(1, m):
            res = self.merge(res, mat[i], k)
        return res[k-1]
    
    # problem 373's solution, find k pairs with smallest sums
    def merge(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        q = [(nums1[i] + nums2[0], i, 0) for i in range(m)]
        heapify(q)
        res = []
        while k and q:
            val, i, j = heappop(q)
            res.append(val)
            j += 1
            if j < n: heappush(q, (nums1[i] + nums2[j], i, j))
            k -= 1
        
        return res