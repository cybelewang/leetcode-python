"""
801 Minimum Swaps To Make Sequences Increasing

We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation: 
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
Note:

A, B are arrays with the same length, and that length will be in the range [1, 1000].
A[i], B[i] are integer values in the range [0, 2000].
"""
# similar problems: 714 Best Time to Buy and Sell Stock with Transaction Fee
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/9311385.html
    # DP with two arrays
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        swap, noswap = [n]*n, [n]*n
        swap[0], noswap[0] = 1, 0
        for i in range(1, n):
            if A[i] > A[i-1] and B[i] > B[i-1]: # no need to swap
                swap[i] = swap[i-1] + 1 # to maintain the increasing order after swap, we need to swap i-1, then swap i
                noswap[i] = noswap[i-1] # no need to swap, so use noswap[i-1]
            
            if A[i] > B[i-1] and B[i] > A[i-1]: # need to swap
                swap[i] = min(swap[i], noswap[i-1] + 1) # i-1 doesn't need to swap
                noswap[i] = min(noswap[i], swap[i-1])   # if we don't swap i, we need to swap i-1 to maintain the increasing order

        return min(swap[-1], noswap[-1])

A = [0,3,5,8,9]
B = [2,1,4,6,9] # expected 1
print(Solution().minSwap(A, B))