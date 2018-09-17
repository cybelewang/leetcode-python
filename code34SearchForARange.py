"""
34 Search for a Range

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

def _search(nums, result, l, r, target):
    if l > r:
        return

    while l <= r:
        mid = (l + r)//2

        if target == nums[mid]:
            result[0] = mid if result[0] == -1 else min(result[0], mid)
            result[1] = max(result[1], mid)

            _search(nums, result, l, mid -1, target)
            _search(nums, result, mid + 1, r, target)

            return
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = [-1, -1]
    if not nums:
        return result

    _search(nums, result, 0, len(nums) - 1, target)
    
    return result

test_cases = [([], 1), ([1], 1), ([1], 0), ([1,1,1,1,1,1],1), ([1,1,1,1,1,1,1,2,2,2,3,3,3,3,3,3], 2), ([5,7,7,8,8,10], 8)]

for nums, target in test_cases:
    print(searchRange(nums, target))