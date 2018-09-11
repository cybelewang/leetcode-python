"""
77 Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""
# great solution https://leetcode.com/problems/combinations/discuss/27024/1-liner-3-liner-4-liner
class Solution(object):
    def _dfs(self, res, build, i, k, n):
        if len(build) == k:
            res.append(build[:])
        else:
            for i in range(i, n+1):
                build.append(i)
                self._dfs(res, build, i + 1, k, n)
                build.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 1 or k > n:
            return []

        res, build = [], []
        self._dfs(res, build, 1, k, n)

        return res
# solution on 9/10/2018
import itertools
class Solution2:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(n, num, k, build, res):
            if k == 0:
                res.append(build[:])
                return

            for i in range(num+1, n+1):
                build.append(i)
                dfs(n, i, k-1, build, res)
                build.pop()
        
        build, res = [], []
        dfs(n, 0, k, build, res)

        return res

    def combine_Library(self, n, k):
        return list(itertools.combinations(range(1, n+1), k))
            
obj = Solution2()
print(obj.combine_Library(4,2))
        