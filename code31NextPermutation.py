"""
31 Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
# similar problems: 556 Next Greater Element III
def swap(nums, i, n):
    j = n - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1 # bug fixed, forgot to advance i
        j -= 1 # bug fixed, forgot to decrease j

def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if not nums or len(nums) < 2:
        return

    n = len(nums)
    i = n - 2
    while i > -1 and nums[i] >= nums[i+1]:
        i -= 1
    
    if i == -1:
        swap(nums, 0, n)
        return

    # i is now at the right most position that is smaller than the next 
    # Find the smallest nums[j] > nums[i], with j in range [i+1, n)
    # We know that after finding i, nums[i+1, n) is in descending order
    j = i + 1
    while j < n and nums[j] > nums[i]:
        j += 1
    j -= 1

    # We have found j, swap nums[i] and nums[j]
    nums[i], nums[j] = nums[j], nums[i]

    # Reorder nums[j:] in descending order
    while (j+1) < n and nums[j] < nums[j+1]:
        nums[j], nums[j+1] = nums[j+1], nums[j]
    
    # Swap the sub array [i+1 : ]
    swap(nums, i+1, n)

# 8/2/2020
def nextPermutation2(nums):
        n = len(nums)
        if n < 1: return
        # find first i with nums[i] < nums[i+1]
        i = n - 2
        while i > -1 and nums[i] >= nums[i+1]:
            i -= 1
        # all nums is in descending order
        if i == -1:
            nums = nums[::-1]
            return
        # from right to left, find first j with nums[j] > nums[i]
        j = n-1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        # swap nums[j] with nums[i]
        nums[i], nums[j] = nums[j], nums[i]
        # reverse the rest of the array
        nums[i+1:] = nums[i+1:][::-1]

# follow-up: previous permutation

test_cases = [[], [0], [0, 1], [1, 2, 3], [3, 2, 1], [1, 1, 5], [1, 3, 4, 2], [1, 4, 3, 2], [4, 1, 3, 5, 2]]
for case in test_cases:
    print(case, end = '')
    print(" -> ", end = '')
    nextPermutation2(case)
    print(case, end='\n')

