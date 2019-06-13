"""
45 Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
"""

def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums or len(nums) < 2:
        return 0

    n = len(nums)
    s, t, steps = 1, nums[0], 0

    while t < n - 1:    # bug fixed: the target should not exceed n - 1, not n
        newT = t
        for i in range(s, t + 1):
            newT = max(newT, i + nums[i])
        s = t + 1 # bug fixed: put s = t + 1 before t = newT, otherwise will cause errors
        t = newT
        steps += 1

    return steps + 1 # bug fixed: use steps + 1 otherwise we missed the last step because t >= n - 1

# 2nd round solution on 6/7/2019, similar to 55 Jump Game
def jump2(nums):
    pre_end, end, N = 0, 0, len(nums)-1
    i, steps = 0, 0
    while end < N:
        while i <= pre_end:
            end = max(end, i + nums[i])
            i += 1
        
        if end == pre_end:
            return -1
        else:
            pre_end = end
            steps += 1
    
    return steps

test_cases = [[],[1],[1,1,1,1],[5, 1, 1, 3, 9, 11],[1,1,0],[2,3,1,1,4]]

for case in test_cases:
    print(case, end = ' -> ')
    print(jump2(case))