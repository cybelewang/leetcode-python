"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        if not nums:
            return res
        # Put the elements into a map to look up the index of the element quickly
        my_dict = {}
        for (i, num) in enumerate(nums):
            res.append([num])
            my_dict[num] = i
        # In each length, we pick up the previously added elements and append an number
        start, end = 1, len(nums) -1
        for length in range(2, len(nums) + 1):
            for i in range(start, end+1):
                sub = res[i]
                for j in range(my_dict[sub[-1]]+1, len(nums)):
                    e = sub[:]
                    e.append(nums[j])
                    res.append(e)
            start = end + 1
            end = len(res) - 1
        
        return res

test_case = [1,2,3,4]
obj = Solution()
print(obj.subsets(test_case))    
            

        