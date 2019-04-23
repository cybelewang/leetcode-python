"""
15 3Sum, three sum

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

# 2nd round solution on 9/16/2018
# time O(N^2), space O(N)
def threeSum2(nums):
    nums.sort()
    n, res = len(nums), []
    right_index = {num:i for i, num in enumerate(nums)}

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:  # a trick to avoid duplicated result, also used in Subsets II, Combination Sum II
            continue
        for j in range(i+1, n):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            need = -(nums[i] + nums[j])
            if need in right_index and right_index[need] > j:
                res.append([nums[i], nums[j], need])

    return res

# 3rd round solution on 4/23/2019
# time O(NlogN), space O(1)
def threeSum3(nums):
    nums.sort()
    res = []
    for k, c in enumerate(nums):
        if k > 0 and nums[k] == nums[k-1]:
            continue
        i, j = k+1, len(nums)-1
        while i < j:
            if nums[i] + nums[j] + c == 0:
                res.append([nums[i], nums[j], c])
                i += 1
                j -= 1
                # need to think duplicated elements
                while i < j and nums[i] == nums[i-1]:
                    i += 1
                while i < j and nums[j] == nums[j+1]:
                    j -= 1
            elif nums[i] + nums[j] + c > 0:
                j -= 1
            else:
                i += 1
        
    return res

test_case = [-2,0,0,2,2]
print(threeSum3(test_case))