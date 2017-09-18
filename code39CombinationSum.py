"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
"""
# First solution with 7%
def _combine(candidates, result, temp, i, cur, target):
    """
    result: the result list
    temp: the temp list which is growing
    i: the current index of sorted candidates
    cur: the current sum of candidates[0:i+1] (not including candidates[i+1])
    """
    if cur == target:
        result.append(temp)
    elif cur > target or i >= len(candidates): # if we put this at top, then a valid list may be ignored by mistake because i == len
        return
    else:
        n = (target - cur)//candidates[i]
        _combine(candidates, result, list(temp), i+1, cur, target)  # include [i] 0 times
        for j in range(n): # include [i] multiple times
            temp.append(candidates[i])
            cur += candidates[i]
            _combine(candidates, result, list(temp), i+1, cur, target)

# Second trial without copying sublists, 14%
def _combine2(candidates, result, temp, i, cur, target):
    """
    result: the result list
    temp: the temp list which is growing and decreasing (like a stack)
    i: the current index of sorted candidates
    cur: the current sum of candidates[0:i+1] (not including candidates[i+1])
    """
    if cur == target:
        result.append(temp[:]) # temp is a pointer, and temp[:] is a list
    elif cur > target or i >= len(candidates): # if we put this at top, then a valid list may be ignored by mistake because i == len
        return
    else:        
        _combine2(candidates, result, temp, i+1, cur, target)  # include [i] 0 times
        n = (target - cur)//candidates[i]

        for j in range(n): # include [i] multiple times
            temp.append(candidates[i])
            cur += candidates[i]
            _combine2(candidates, result, temp, i+1, cur, target)
        
        for j in range(n):
            temp.pop()
            cur -= candidates[i]

# [BEST] General solution for back tracking, about 21%
def _backtrack(candidates, result, temp, remain, start):
    if remain < 0: return
    elif remain == 0: result.append(temp[:])
    else:
        for i in range(start, len(candidates)):
            temp.append(candidates[i])
            _backtrack(candidates, result, temp, remain - candidates[i], i)
            temp.pop()

def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()

    result = []
    temp = []
    i, cur = 0, 0
    _combine2(candidates, result, temp, i, cur, target)
    #_backtrack(candidates, result, temp, target, 0)

    return result

candidates = [5,1,2,3]
print(combinationSum(candidates, 6))