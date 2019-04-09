"""
1004 Max Consecutive Ones III

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s. 

Example 1:
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]

Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1 
"""
class Solution:
    # https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC%2B%2BPython-Sliding-Window
    # we don't need to reduce the the size of sliding window.
    # as we want to find the maximum window.
    def longestOnes_OJ(self, A, K):
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1
    # sliding window from OJ discuss
    def longestOnes(self, A, K):
        """
        :type A: list[int]
        :type K: int
        :rtype: int
        """
        i, j = 0, 0
        res = 0
        for j in range(len(A)):
            if not A[j]:
                K -= 1                
                if K < 0:
                    # find the next position i with A[i] == 0
                    while i <= j and A[i] == 1:
                        i += 1
                    # and pass this 0
                    i += 1
                    K += 1
            
            res = max(res, j - i + 1)

        return res

A, K = [0], 0   # expect 0
A, K = [0], 1   # expect 1
A, K = [1], 0   # expect 1
A, K = [1], 1   # expect 1
A, K = [1, 1, 1, 0, 1, 1, 1], 0    # expect 3
A, K = [0, 1, 1, 1, 0, 0, 1, 1, 1], 1 # expect 4
A, K = [0, 0, 1, 1, 1, 0, 1], 1 # expect 5
A, K = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3   # expect 10
print(Solution().longestOnes(A, K))