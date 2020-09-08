"""
995 Minimum Number of K Consecutive Bit Flips

In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.

Example 1:

Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].
Example 2:

Input: A = [1,1,0], K = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].
Example 3:

Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
 
Note:

1 <= A.length <= 30000
1 <= K <= A.length
"""
class Solution:
    # greedy method
    # For each 0, we should flip it and the next K-1 bits, but we don't actually do that because we can use a target to represent the matching bit
    # When we flip a 0 to 1, we change the target to 0, so if the next bit is not 0, it should be flipped again
    # In general, we have an initial target of 1, then every time we check if current number is equal to target, if not, this means this bit needs to be flipped
    # Then we flip the bit by incrementing ans, but we also need to flip target, and also mark i + K as 1 in the mark array so when we iterate to i + K, the target will be flipped again
    def minKBitFlips(self, A: List[int], K: int) -> int:
        target, n = 1, len(A)
        mark = [0]*n
        count = 0
        for i in range(n):
            target ^= mark[i]
            if A[i] != target:
                # flip this number
                count += 1
                target ^= 1
                end = i + K
                if end > n: return -1
                if end < n: mark[end] = 1
        return count