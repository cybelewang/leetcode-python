"""
33 Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

def search(nums, target):
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

        if nums[l] <= nums[r]:
            # not-rotated array, binary search
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        elif nums[mid] < nums[l]:
            # rotated less than half length
            if target > nums[mid] and target <= nums[r]: # bug fixed, previously it was target < nums[r], which should be target <= nums[r]
                l = mid + 1
            else:
                r = mid - 1
        else:
            # rotated >= half length
            if target >= nums[l] and target < nums[mid]: # bug fixed, previously it was target > nums[l], which should be target >= nums[l], try nums = [3,5,1] and target = 3
                r = mid - 1
            else:
                l = mid + 1
    
    return -1

# 2nd round solution on 6/16/2019
# see OneNote
def search2(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l + r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] <= nums[r]:
            # non-rotated, or rotated less than half length
            # right half must be sorted, so we check if target is in right half
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            # nums[mid] > nums[r]
            # rotated more than half length
            # left half must be sorted, so we check if target is in left half
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
    return -1


test_cases = [([], 0), ([1], 2), ([3, 2], 1), ([3,5,1], 3),([4,5,6,7,0,1,2], 0)]

for nums, target in test_cases:
    print(search2(nums, target))