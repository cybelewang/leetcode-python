"""
41 First Missing Positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i, n = 0, len(nums)
    while i < n:
        if nums[i] < 1 or nums[i] > n or nums[i] == i + 1:
            i += 1
        elif nums[nums[i] - 1] != nums[i]: # bug fixed. If we don't check this, it could lead to a dead loop, for example, nums = [2, 2, 2, 2]
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    i = 0
    # Pitfall! We should not use for loop because it may stop at i = n - 1, consider nums = [1]
    # for i in range(n):
    #     if nums[i] != i + 1:
    #         break 
   
    while i < n and nums[i] == i + 1:
        i += 1
    
    return i + 1

# 2nd round solution on 9/18/2018
def firstMissingPositive2(nums):
    n = len(nums)
    for i in range(n):
        while 0 < nums[i] < n + 1 and nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    
    # now check each position's number, see if its value is i + 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n+1

test_cases = [[], [1], [1, 2, 0], [3, 4, -1, 1], [2, 2, 2, 2, 2]]

for case in test_cases:
    print(case, end = ' -> ')
    print(firstMissingPositive2(case))
