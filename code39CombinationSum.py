"""
39 Combination Sum

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
class Solution:
    # First solution with 7%
    def _combine(self, candidates, result, temp, i, cur, target):
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
            self._combine(candidates, result, list(temp), i+1, cur, target)  # include [i] 0 times
            for j in range(n): # include [i] multiple times
                temp.append(candidates[i])
                cur += candidates[i]
                self._combine(candidates, result, list(temp), i+1, cur, target)

    # Second trial without copying sublists, 14%
    def _combine2(self, candidates, result, temp, i, cur, target):
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
            self._combine2(candidates, result, temp, i+1, cur, target)  # include [i] 0 times
            n = (target - cur)//candidates[i]

            for j in range(n): # include [i] multiple times
                temp.append(candidates[i])
                cur += candidates[i]
                self._combine2(candidates, result, temp, i+1, cur, target)
            
            for j in range(n):
                temp.pop()
                cur -= candidates[i]

    # [BEST] General solution for back tracking, about 21%
    def _backtrack(self, candidates, result, temp, remain, start):
        if remain < 0: return
        elif remain == 0: result.append(temp[:])
        else:
            for i in range(start, len(candidates)):
                temp.append(candidates[i])
                self._backtrack(candidates, result, temp, remain - candidates[i], i)
                temp.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()

        result = []
        temp = []
        i, cur = 0, 0
        #self._combine2(candidates, result, temp, i, cur, target)
        self._backtrack(candidates, result, temp, target, 0)

        return result

# 2nd round solution on 9/12/2018
class Solution2:
    # my own solution with bug fixed
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, start, curSum, target, build, res):
            if curSum >= target:
                if curSum == target:
                    res.append(build[:])
                return
            # bug fixed: we should consider reuse candidates[start] separately, or see below combinationSum2()
            build.append(candidates[start])
            dfs(candidates, start, curSum + candidates[start], target, build, res)
            build.pop()
            # bug fixed: the start range was "start", which was wrong, should be start + 1
            for i in range(start + 1, len(candidates)):
                num = candidates[i]
                build.append(num)
                curSum += num
                dfs(candidates, start + 1, curSum, target, build, res)
                curSum -= num
                build.pop()
        
        # main
        res = []
        dfs(candidates, 0, 0, target, [], res)

        return res

    # help from OneNote
    def combinationSum2(self, candidates, target):
        def dfs(candidates, start, remain, build, res):
            if remain < 0:
                return
            elif remain == 0:
                res.append(build[:])
            else:
                for i in range(start, len(candidates)):
                    build.append(candidates[i])
                    dfs(candidates, i, remain - candidates[i], build, res)  # bug fixed: second parameter should not use "start", but should be "i", so we will never revisit candidates[0] ... candidates[i-1]
                    build.pop()
        # main
        candidates.sort()
        res = []
        dfs(candidates, 0, target, [], res)

        return res

candidates = [2, 3, 6, 7]
print(Solution2().combinationSum(candidates, 7))