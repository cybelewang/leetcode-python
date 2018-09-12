"""
90 Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""
# similar problems: 78 Subsets; 491 Increasing Subsequences;
# TODO: try to solve it using problem 491's solution
class Solution:
    def countLastNumber(self, sub):
        j, count = len(sub) - 2, 1
        while j > -1 and sub[j] == sub[-1]:
            j -= 1
            count += 1
        
        return count

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        # Generate a histogram dictionary for all the numbers
        hist = {}   # key: unique number, value: repeated times
        for num in nums:
            if num in hist:
                hist[num] += 1
            else:
                hist[num] = 1 

        unique = list(hist) # list of the unique numbers
        res = [[]]  # empty subset always there
        
        index = {}  # As Subset I, we save the unique number and its index in "unique" to look for the index quickly
        for (i, num) in enumerate(unique):
            index[num] = i
            res.append([num])

        start, end = 1, len(res)

        for length in range(2, len(nums) + 1):
            for i in range(start, end):
                sub = res[i]
                # Add the same last number, if not exceed the repeated times
                if self.countLastNumber(sub) < hist[sub[-1]]:
                    e = sub[:]
                    e.append(sub[-1])
                    res.append(e)
                # Add each of the remaining numbers 
                for j in range(index[sub[-1]] + 1, len(unique)):
                    e = sub[:]
                    e.append(unique[j])
                    res.append(e)
            
            start = end
            end = len(res)
        
        return res

# 2nd solution on 9/12/2018, similar to 78 Subset
class Solution2:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, start, build, res):
            res.append(build[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:  # the difference between this problem and 78 Subsets I
                    continue
                build.append(nums[i])
                dfs(nums, i+1, build, res)
                build.pop()
        
        nums.sort() # after sorting, same numbers must be together
        res = []
        dfs(nums, 0, [], res)

        return res

nums = [1,2,2]
obj = Solution2()
print(obj.subsetsWithDup(nums))