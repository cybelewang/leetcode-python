"""
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

obj = Solution()
print(obj.combine(4,1))
        