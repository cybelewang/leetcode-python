"""
47 Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
# similar problems: 46 Permutations; 90 Subsets II
class Solution:
    def _permuteUnique(self, nums, res, build, used, remain):
        if (remain == 0):
            res.append(build[:])
        else:
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue

                build.append(nums[i])
                used[i] = True
                self._permuteUnique(nums, res, build, used, remain - 1)
                build.pop()
                used[i] = False

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 1:
            return []

        nums.sort()

        used = [False]*len(nums)
        res = []
        self._permuteUnique(nums, res, [], used, len(nums))

        return res

# 2nd round solution on 9/12/2018
from itertools import permutations
class Solution2:
    # dfs solution with help from OneNote
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, start, build, used, res):
            if len(build) == len(nums):
                res.append(build[:])
                return
            
            for i in range(0, len(nums)):
                if used[i] or (i > 0 
                and 
                nums[i] == nums[i-1] 
                and 
                not used[i-1]):   # we need to make sure the same values are used in sequence, or nums[i-1] must be in left of nums[i] if they are equal
                    continue
                
                build.append(nums[i])
                used[i] = True
                dfs(nums, i+1, build, used, res)
                used[i] = False
                build.pop()

        nums.sort()
        used, res = [False]*len(nums), []
        dfs(nums, 0, [], used, res)

        return res

    def permuteUnique_Library(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(set(permutations(nums)))

test_case = [1, 1, 2]
print(Solution2().permuteUnique(test_case))        