"""
969 Pancake Sorting

Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  
We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
Example 2:

Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.

Note:

1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]
"""
class Solution:
    # for length i subarray A[:i], we find the index max_pos which has maximum value in A[:i], then we rotate A[max_pos] with A[0], then rotate first i elements in A to put A[max_pos] in A[i-1]
    # need to handle when max_pos == 0
    def pancakeSort(self, A):
        """
        :type A: list[int]
        :rtype: list[int]
        """
        def rotateK(A, K, res):
            """
            rotate first K elements in A
            also record K to result list
            """
            if K < 2:   # bug fixed: we should not rotate first 0 and first 1 elements
                return
            res.append(K)
            left, right = 0, K-1
            while left < right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        # main
        N, res = len(A), []
        for i in range(N, 1, -1):
            # find the index with max value in A[:i]
            max_pos = 0
            for j in range(1, i):
                if A[j] > A[max_pos]:
                    max_pos = j

            rotateK(A, max_pos + 1, res)    # rotate A[max_pos] to A[0]
            rotateK(A, i, res)  # rotate A[0] to A[i-1]

        # print(A)
        return res

A = [3, 2, 4, 1]
print(Solution().pancakeSort(A))
