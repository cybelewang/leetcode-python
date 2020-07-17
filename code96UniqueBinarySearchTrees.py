"""
96 Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
# Use binary search strategy and dict to save recursive result
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #return self._numSubTrees(1, 1, n, n)
        #return self._numSubTrees2(1, n)
        #return self._numSubTrees3(1, n, {})
        return self._dp(n)

    # Solution 1, minVal and maxVal seem to be redundant
    def _numSubTrees(self, minVal, s, e, maxVal): 
        """
        number of subtrees with minimal value s, and maximum value e, minVal/maxVal is the min/max value for all nodes in this subtree
        :type minVal: int
        :type maxVal: int
        :type s: int
        :type e: int
        :rtype: int
        """
        if s > e or s > maxVal or e < minVal:
            return 1    # "None"

        res = 0
        for i in range(s, e+1):
            left = self._numSubTrees(minVal, s, i - 1, min(i-1, maxVal))    # number of unique BSTs as left subtree
            right = self._numSubTrees(max(i+1, minVal), i+1, e, maxVal)     # number of unique BSTs as right subtree
            res += left * right
        
        return res
    
    # Solution 2: use only two boundaries
    def _numSubTrees2(self, s, e):
        """
        number of subtrees with minimal value s, and maximum value e
        :type s: int
        :type e: int
        :rtype: int
        """
        if s > e:
            return 1    # "None"

        res = 0
        for i in range(s, e+1):
            left = self._numSubTrees2(s, i - 1) # number of unique BSTs as left subtree
            right = self._numSubTrees2(i+1, e)  # number of unique BSTs as right subtree
            res += left * right
        
        return res
    
    # Solution 3: use only two boundaries and dictionary to accelerate
    def _numSubTrees3(self, s, e, history):
        """
        number of subtrees with minimal value s, and maximum value e
        :type s: int
        :type e: int
        :type history: dict{(int, int): int}
        :rtype: int
        """
        if s > e:
            return 1    # "None"
        
        if (s, e) in history:
            return history[(s, e)]
        else:
            res = 0
            for i in range(s, e+1):
                left = self._numSubTrees3(s, i - 1, history) # number of unique BSTs as left subtree
                right = self._numSubTrees3(i+1, e, history)  # number of unique BSTs as right subtree
                res += left * right
                
            history[(s, e)] = res   # save to history
            return res

    def _dp(self, n):
        """
        Dynamic programming method, see previous Java solution
        """
        G = [0 for i in range(n+1)]
        G[0] = 1
        G[1] = 1

        for i in range(2, n+1):
            for j in range(1, i + 1):
                G[i] += G[j-1]*G[i-j]

        return G[n]

    # 7/15/2020
    # 2D DP solution, dp[i][j] represents the number of unique BSTs in range i to j inclusive, see OneNote
    def numTrees4(self, n):
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n, 0, -1):
            dp[i][i] = 1
            for j in range(i+1, n+1):
                for k in range(i, j+1):
                    left = 1 if k==i else dp[i][k-1]
                    right = 1 if k==j else dp[k+1][j]
                    dp[i][j] += left * right
        return dp[1][n]

    # 7/15/2020
    # 1D DP solution, dp[i] represents the number of unique BSTs with length i because we don't care the start number.
    # See OneNote
    def numTrees5(self, n):
        dp = [0]*(n+1)
        dp[0] = 1 # empty subtree also counts as 1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j]
        return dp[n]

obj = Solution()
print(obj.numTrees5(4))
