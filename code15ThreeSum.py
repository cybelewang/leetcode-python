"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    nums.sort()

    for i in range(len(nums)-2):
        if (i > 0) and (nums[i] == nums[i-1]):
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                result.append([nums[i],nums[l],nums[r]])
                l += 1
                r -= 1                
                while (l < r) and nums[l]==nums[l-1]: # bug fixed
                    l += 1
                while (l < r) and nums[r]==nums[r+1]: # bug fixed
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1      
    
    return result

test_case = [-2,0,0,2,2]
print(threeSum(test_case))