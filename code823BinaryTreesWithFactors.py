"""
823 Binary Trees With Factors

Given an array of unique integers, each integer is strictly greater than 1.

We make a binary tree using these integers and each number may be used for any number of times.

Each non-leaf node's value should be equal to the product of the values of it's children.

How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

Example 1:

Input: A = [2, 4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: A = [2, 4, 5, 10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 

Note:

1 <= A.length <= 1000.
2 <= A[i] <= 10 ^ 9.
"""
class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for j in range(i):
                if x % A[j] == 0: #A[j] will be left child
                    right = x // A[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD

        return sum(dp) % MOD

    # 1st trial, wrong solution
    def numFactoredBinaryTrees2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        M = 10**9 + 7
        A.sort()
        n, count = len(A), {}

        res = 0
        for i in range(n):
            cnt = 1
            for j in range(i):
                if A[i] % A[j] == 0 and A[i]//A[j] in count:
                    # if A[j] == A[i]//A[j]:
                    #     cnt += count[A[j]]
                    # else:
                    #     cnt += count[A[j]] * count[A[i]//A[j]]
                    # bug fixed: we don't need the above commented code, because the problem states that no duplicates in A, so 
                    cnt += count[A[j]] * count[A[i]//A[j]]
            
            count[A[i]] = cnt % M
            res = (res + count[A[i]])%M
        
        return res

A = [2, 4]
#A = [2, 4, 5, 10]
#A = [45,42,2,18,23,1170,12,41,40,9,47,24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43,15,4,16,35,25,20,44,5,48]  # expected 777
print(Solution().numFactoredBinaryTrees2(A))