"""
16 3Sum Closest, three sum closest
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
from math import fabs
def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    minDiff = 2**31 - 1 # max int in a 32 bit platform
    result = 0

    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == target:
                return s
            elif s > target:
                diff = s - target
                if diff < minDiff:
                    result = s
                    minDiff = diff
                r -= 1
            else:
                diff = target -s
                if diff < minDiff:
                    result = s
                    minDiff = diff
                l += 1

    return result

# 2nd visit on 4/24/2019
def threeSumClosest2(nums, target):
    nums.sort()
    res = sum(nums[:3])
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        j, k = i+1, len(nums)-1
        while j < k:
            s = a + nums[j] + nums[k]
            if abs(s-target) < abs(res-target):
                res = s
            if s < target:
                j += 1
            else:
                k -= 1
    
    return res


test_case = [-1, 2, 1, -4]
print(threeSumClosest2(test_case, 1))