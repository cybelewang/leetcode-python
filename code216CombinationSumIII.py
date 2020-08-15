"""
216 Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""
from itertools import combinations
class Solution:
    # use 
    def combinationSum(self, k: int, n: int) -> List[List[int]]:
        return [c for c in combinations(range(1,10), k) if sum(c) == n]

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(build, start, target, res):
            # corner cases
            curSum = sum(build)
            if curSum > target:
                return
            if len(build) == k:
                if curSum == target:
                    res.append(build[:])
                return
            
            for i in range(start, 10):
                build.append(i)
                helper(build, i+1, target, res)
                build.pop()
            
        res = []
        helper([], 1, n, res)
        return res

obj = Solution()
print(obj.combinationSum3(3, 7))    
