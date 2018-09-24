"""
440 K-th Smallest in Lexicographical Order

Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.
Note: 1 ≤ k ≤ n ≤ 10^9.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
"""
class Solution:
    # decimal tree, each node could have up to 10 child nodes
    # pre-order traversal on the decimal tree
    # http://www.cnblogs.com/grandyang/p/6031787.html
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        cur, k = 1, k-1
        while k:
            step, first, last = 0, cur, cur + 1
            # get the number of nodes with the "prefix" cur
            # for example, when cur is 1, the below while loop will get all number of nodes starting with '1', like '1', '100', '1234', as long as these nodes' values <= n
            while first <= n:
                step += min(n+1, last) - first
                first *= 10
                last *= 10
            
            if step <= k:
                cur += 1   # go to next sibling
                k -= step
            else:
                cur *= 10   # go to first child
                k -= 1
        
        return cur

    # Solution similar to 386, TLE
    def findKthNumber2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        stack = list(range(min(9, n), 0, -1))
        count = 0
        while stack:
            cur = stack.pop()
            count += 1
            if count == k:
                return cur
            if cur*10 <= n:
                # stack.extend(range(min(cur*10 + 9, n), cur*10 + 1, -1))   # bug fixed: the stop in range should be cur*10 - 1, not cur*10 + 1 because step is -1
                stack.extend(range(min(cur*10 + 9, n), cur*10 - 1, -1))
        return n

obj = Solution()
print(obj.findKthNumber(10**9,10**8))
#print(obj.findKthNumber(13,2))