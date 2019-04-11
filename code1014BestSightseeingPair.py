"""
1014 Best Sightseeing Pair

Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.
The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:

Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

Note:

2 <= A.length <= 50000
1 <= A[i] <= 1000
"""
from functools import reduce
class Solution:
    # https://leetcode.com/problems/best-sightseeing-pair/discuss/260850/JavaC%2B%2BPython-One-Pass
    # def maxScoreSightseeingPair_oneline(self, A):
    #     return reduce(lambda (r, c), a: [max(r, c + a), max(c, a) - 1], A, [0, 0])[0]
    
    """
    O(1) space, O(N) time
    Explanation
    cur will record the best score that we have met.
    We iterate each value a in the array A,
    update res by max(res, cur + a)

    Also we can update cur by max(cur, a).
    Note that when we move forward,
    all sightseeing spot we have seen will be 1 distance further.

    So for the next sightseeing spot cur = Math.max(cur, a) **- 1**

    It's kinds of like, "A near neighbor is better than a distant cousin."
    """
    # two parts: A[i] - (j - i) and A[j]
    # below "cur" is the current max of A[i] - (j-i), as j iterates, every time minus 1
    # below "res" is the current max of A[j] + cur
    def maxScoreSightseeingPair_OJ(self, A):
        cur = res = 0
        for a in A:
            res = max(res, cur + a)
            cur = max(cur, a) - 1
        return res

    # my own solution
    # the idea is to separate the result to two parts A[i] + i and A[j] - j
    # we can get A[i] + i by iterate A, but for each position i, we need to know largest A[j] - j with j > i
    # we can preprocess A[j] - j by iterating j from right to left. When A[j] - j becomes larger, we push j into stack.
    # then we iterate i from left to right, for each i, if i is in stack's top, we pop it so stack exposes the index j for largest A[j] - j
    def maxScoreSightseeingPair(self, A):
        """
        :type A: list[int]
        :rtype: int
        """
        # cache max(A[j] - j)
        # then iterate A and update max of A[i] + i + A[j] - j, where j > i
        N = len(A)
        stack = [N-1]   # stack saves the index j, where for any k > j, A[k] - k < A[j] - j
        for j in range(N-2, 0, -1): # iterate from right to left
            last = stack[-1]    # last index k in stack which has biggest A[k] - k
            if A[j] - j > A[last] - last:
                stack.append(j)
        
        res = -2**31
        for i in range(N-1):
            if i == stack[-1]:  # expose the biggest A[j] - j for j > i
                stack.pop()
            j = stack[-1]
            res = max(res, A[i] + i + A[j] - j)
        
        return res

A = [1, 1]  # expect 1
A = [3, 2, 1, 5] # expect 5
A = [8,1,5,2,6] # expect 11
print(Solution().maxScoreSightseeingPair_OJ(A))