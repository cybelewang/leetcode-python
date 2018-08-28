"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""
# similar problems: 416 Partition Equal Subset Sum;
class Solution:
    # wrong solution, TLE, dfs will go to a dead loop due to lack of paramter start
    def canPartitionKSubsets2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum_ = sum(nums)
        if sum_ % k != 0:   return False
        
        target = sum_ // k
        nums.sort()

        n = len(nums)
        used = [False]*n

        def dfs(nums, used, target, cursum, k):
            if cursum > target:
                return False
            elif cursum == target:
                if k == 1:
                    return True
                else:
                    return dfs(nums, used, target, 0, k-1)
            else:
                res = False
                for i in range(n):
                    if nums[i] + cursum > target:
                        break
                    else:
                        if not used[i]:
                            used[i] = True
                            res = res or dfs(nums, used, target, cursum + nums[i], k)
                            used[i] = False
                
                return res
        
        return dfs(nums, used, target, 0, k)

nums, k = [4,5,3,2,5,5,5,1,5,5,5,5,3,5,5,2], 13
print(Solution().canPartitionKSubsets2(nums, k))