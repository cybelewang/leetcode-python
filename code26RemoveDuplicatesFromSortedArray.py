"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 1 : return 0
    i = 1
    for j in range(1, len(nums)):
        if nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i += 1
    
    return i

test_cases = [[],[1],[1,2,3],[1,1,2],[1,1,1,1,1,1]]

for case in test_cases:
    print(removeDuplicates(case), end='\n')