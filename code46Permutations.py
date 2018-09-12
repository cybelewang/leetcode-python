"""
46 Permutations

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""
# similar problems: 47 Permutations II
class Solution:
    def _permute(self, nums, res, build, used, remain):
        if remain == 0:
            res.append(build[:])
        else:
            for i in range(len(nums)):
                if not used[i]:
                    build.append(nums[i])
                    used[i] = True
                    self._permute(nums, res, build, used, remain - 1)
                    build.pop()                
                    used[i] = False

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 1:
            return []

        used = [False for i in range(len(nums))]
        res = []
        self._permute(nums, res, [], used, len(nums))

        return res

# 2nd round solution on 9/12/2018
from itertools import permutations
class Solution2:
    # using permutations library
    def permute_Library(self, nums):
        return list(permutations(nums))
    
    # using recursive solution, same as 1st round solution
    def permute_DFS(self, nums):
        def dfs(nums, selected, build, res):
            if len(nums) == len(build):
                res.append(build[:])
                return
            for i, num in enumerate(nums):
                if selected[i]:
                    continue
                build.append(num)
                selected[i] = True
                dfs(nums, selected, build, res)
                selected[i] = False
                build.pop()
    
        selected, res = [False]*len(nums), []
        dfs(nums, selected, [], res)

        return res

    # solution 2 from http://www.cnblogs.com/grandyang/p/4358848.html
    # swap two numbers in nums, and all permutations can be got through recursive call
    def permute_Swap(self, nums):
        def dfs(nums, start, res):
            if start == len(nums):
                res.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                dfs(nums, start + 1, res)
                nums[start], nums[i] = nums[i], nums[start]

        # main
        res = []
        dfs(nums, 0, res)

        return res

test_case = [1, 3, 2]
obj = Solution2()
print(obj.permute_Swap(test_case))