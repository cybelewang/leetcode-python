"""
41 First Missing Positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""
# https://leetcode.com/problems/first-missing-positive/solution/
# mark presence by changing that position's number to negative
def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # if no 1 present in array, return 1
    if nums.count(1) == 0: return 1
    n = len(nums)
    # change non-positive and > n numbers to 1
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1
    # now array's values must be between 1 and n (inclusive)
    # mark each present position's value to negative
    for i in range(n):
        j = abs(nums[i]) - 1
        nums[j] = -1 * abs(nums[j])
    
    # first check 1 to n-1 position
    for i in range(n):
        if nums[i] > 0: return i

    # then the first missing must be n + 1
    return n + 1

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
