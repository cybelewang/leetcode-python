"""
35 Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

"""
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r)//2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    
    return l

# 2nd round solution on 9/17/2018
def searchInsert2(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right)//2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return right

test_cases = [([], 0), ([2], 0), ([2], 3), ([1, 3, 5, 6], 5), ([1, 3, 5, 6], 2), ([1, 3, 5, 6], 7), ([1, 3, 5, 6], 0)]

for nums, target in test_cases:
    print(nums,end=', ')
    print(target, end=' -> ')
    print(searchInsert2(nums, target))