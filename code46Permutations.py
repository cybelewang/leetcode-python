"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""
def _permute(nums, res, build, used, remain):
    if remain == 0:
        res.append(build[:])
    else:
        for i in range(len(nums)):
            if not used[i]:
                build.append(nums[i])
                used[i] = True
                _permute(nums, res, build, used, remain - 1)
                build.pop()                
                used[i] = False

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums or len(nums) < 1:
        return []

    used = [False for i in range(len(nums))]
    res = []
    _permute(nums, res, [], used, len(nums))

    return res

test_case = [1, 3, 2]
print(permute(test_case))