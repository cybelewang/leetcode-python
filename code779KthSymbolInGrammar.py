"""
779 K-th Symbol in Grammar

On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].
"""
class Solution:
    # my own solution using binary search
    # 1. we can find that in row N, there are 2**(N-1) elements
    # 2. if K <= 2**(N-2), then it must be in the left half of row N, otherwise it must be in the right half of row N
    # 3. so we use a recursive function, if we search to the left half, we use the same root, otherwise we alternative root between 0 and 1
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        def search(root, N, K):
            if N == 1:
                return root
            count = 2**(N-1)
            if K > count//2:
                return search(root^1, N-1, K - count//2)
            else:
                return search(root, N-1, K)

        return search(0, N, K)

print(Solution().kthGrammar(30, 2**29))