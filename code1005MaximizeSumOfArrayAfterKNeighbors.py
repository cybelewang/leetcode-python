"""
1005 Maximize Sum Of Array After K Negations

Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  
(We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.

Example 1:
Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].

Example 2:
Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].

Example 3:
Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].

Note:

1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100
"""
class Solution:
    # distribute K with below priorities
    # 1. negative numbers from smallest to biggest, if K is not engough to cover all these negative numbers, return
    # 2. if A has 0, we can put all remaining K to 0, return
    # 3. if A has no 0, and remaining K is even, we can put all remainging K to any single positive number, return
    # 4. if there is no 0, and remaining K is odd, we turn smallest positive number to negative
    # the above 1, 2, 3 can combine to one case
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: list[int]
        :type K: int
        :rtype: int
        """
        negatives, min_abs = [], 100
        ans = 0
        for a in A:
            ans += a
            if a < 0:
                negatives.append(a)
            min_abs = min(min_abs, abs(a))
        
        # distribute K to negatives list
        negatives.sort(reverse = True)  # smallest negative value will be at the end
        while negatives and K > 0:
            ans -= 2*negatives.pop()
            K -= 1
        
        if not negatives and K % 2:
            return ans - 2*min_abs  # case 4
        else:
            return ans  # case 1, 2, 3

A, K = [-1, -2, -3], 2  # expect 4
A, K = [4, 2, 3], 2 # expect 9
A, K = [4, 2, 3], 1 # expect 5
A, K = [3,-1,0,2], 3 # expect 6
print(Solution().largestSumAfterKNegations(A, K))
