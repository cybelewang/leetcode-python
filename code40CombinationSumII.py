"""
40 Combination Sum II

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""
# first trial
def _dfs(candidates, result, sub, remain, start):
    if remain == 0:
        result.append(sub[:])
    elif remain < 0 or start >= len(candidates): # the condition start >= len(candidates) is redundant because the else branch will check it
        return
    else:
        i = start
        while i < len(candidates):        
            sub.append(candidates[i])
            _dfs(candidates, result, sub, remain - candidates[i], i + 1)
            sub.pop()  
            i += 1                      
            while i < len(candidates) and candidates[i] == candidates[i-1]: # try not to use nested while loop
                i += 1

# [BEST] backtrack solution
def _dfs2(candidates, result, sub, remain, start):
    if remain == 0:
        result.append(sub[:])
    elif remain < 0:
        return
    else:
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]: 
                continue         
            sub.append(candidates[i])
            _dfs(candidates, result, sub, remain - candidates[i], i + 1)
            sub.pop()  

def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()

    result = []
    _dfs2(candidates, result, [], target, 0)

    return result

# 2nd round solution on 9/12/2018
class Solution2:
    def combinationSum2(self, candidates, target):
        def dfs(candidates, start, remain, build, res):
            if remain < 0:
                return
            elif remain == 0:
                res.append(build[:])
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue

                    build.append(candidates[i])
                    dfs(candidates, i + 1, remain - candidates[i], build, res)
                    build.pop()
        
        candidates.sort()
        res = []
        dfs(candidates, 0, target, [], res)

        return res
                    

test = [10, 1, 2, 7, 6, 1, 5]
print(Solution2().combinationSum2(test, 8))    