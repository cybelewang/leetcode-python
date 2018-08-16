"""
You have 4 cards each containing a number from 1 to 9. 
You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""
class Solution:
    # reference to http://www.cnblogs.com/grandyang/p/8395062.html  
    # DFS solution
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        eps = 0.001

        def dfs(nums, ops):
            n = len(nums)
            if n == 1:
                return abs(nums[0] - 24) < eps
            
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    t = [nums[k] for k in range(n) if k != i and k != j]
                    for op in ops:
                        if (op == '+' or op == '*') and (i > j):    # if i > j, we already tested nums[i] + nums[j] or nums[i]*nums[j] previously
                            continue
                        if op == '/' and abs(nums[j]) < eps:    # cannot divide zero
                            continue

                        if op == '+':
                            t.append(nums[i]+nums[j])
                        elif op == '-':
                            t.append(nums[i]-nums[j])
                        elif op == '*':
                            t.append(nums[i]*nums[j])
                        else:
                            t.append(nums[i]/nums[j])
                        
                        if dfs(t, ops):
                            return True
                        t.pop() # bug fixed: forgot to restore t
            
            return False

        # main
        ops = ['+', '-', '*', '/']

        return dfs(nums, ops)

nums = [1, 2, 1, 2]
print(Solution().judgePoint24(nums))