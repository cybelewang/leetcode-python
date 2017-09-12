"""
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
            if target > nums[mid] and target < nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            # rotated >= half length
            if target > nums[l] and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
    
    return -1

test_cases = [([], 0), ([1], 2), ([1, 0], 1), ([4,5,6,7,0,1,2], 0)]

for nums, target in test_cases:
    print(search(nums, target))