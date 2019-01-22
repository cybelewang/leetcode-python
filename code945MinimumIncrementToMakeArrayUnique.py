"""
945 Minimum Increment to Make Array Unique

Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

Note:

0 <= A.length <= 40000
0 <= A[i] < 40000
"""
class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 1:
            return 0

        A.sort()
        ans = 0
        candidate = A[0] + 1

        for i in range(1, len(A)):
            if A[i] >= candidate:
                candidate = A[i] + 1
            else:
                ans += candidate - A[i]
                candidate += 1
        
        return ans

#A = []
#A = [1, 2, 2]
#A = [3,2,1,2,1,7]
A = [1, 2, 3, 99]
print(Solution().minIncrementForUnique(A))
