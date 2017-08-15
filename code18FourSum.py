"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    result = []
    nums.sort()

    for i in range(0,len(nums)-3):
        if (i > 0) and (nums[i] == nums[i-1]):
            continue
        for j in range(i+1, len(nums)-2):
            if (j > i + 1) and (nums[j] == nums[j-1]): # bug fixed. Don't forget condition (j > i + 1)
                continue
            k, l = j + 1, len(nums)-1
            while k < l:
                s = nums[i] + nums[j] + nums[k] + nums[l]
                if s == target:
                    result.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k-1]:
                        k += 1
                    while k < l and nums[l] == nums[l+1]:
                        l -= 1
                elif s < target:
                    k += 1
                else:
                    l -= 1
    
    return result

test_case = [1, 0, -1, 0, -2, 2]
print(fourSum(test_case, 1))
      