"""
698 Partition to K Equal Sum Subsets

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
    def canPartitionKSubsets_OJBest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # corner case check
        if len(nums) < k:   return False
        if k == 1:  return True
        s = sum(nums)
        if s%k != 0:    return False
        target = s//k
        nums.sort(reverse=True)
        used = [False]*len(nums)
        start = 0
        for i in range(k-1):
            if not self.helper(nums, target, used, start):
                return False
            while used[start]:
                start += 1
        return True
    
    def helper(self, nums, target, used, start):
        for i in range(start, len(used)):
            if used[i]: continue
            if nums[i] > target:
                continue
            if nums[i] == target or self.helper(nums, target-nums[i], used, i+1):
                used[i] = True
                return True
        return False
    # http://bookshadow.com/weblog/2017/10/15/leetcode-partition-to-k-equal-sum-subsets/
    # DFS + MAP
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dmap = {}
        def solve(nums, target, k):
            if k == 1: return sum(nums) == target
            key = (tuple(nums), k)
            if key in dmap: return dmap[key]
            size = len(nums)
            ans = False
            for x in range(1 << size):  # binary 1 and 0 represent if that number is used, range(1<<size) contains all cases
                sums = 0
                rest = []
                for y in range(size):
                    if (x >> y) & 1:  sums += nums[y]
                    else: rest.append(nums[y])
                if sums == target and solve(rest, target, k - 1):
                    ans = True
                    break
            dmap[key] = ans
            return ans
        
        # main
        sums = sum(nums)
        if sums % k: return False
            
        return solve(sorted(nums), sums // k, k)
    
    # typical DFS solution, easier to understand
    # trick to sort nums in reversed order, so we can quickly get current sum > target
    # from http://www.cnblogs.com/grandyang/p/7733098.html
    def canPartitionKSubsets2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum_ = sum(nums)
        if sum_ % k: return False
        
        target = sum_ // k
        nums.sort(reverse=True)
        used = [False]*len(nums)

        def dfs(nums, used, target, cursum, k, start):
            if k == 1: return True
            if cursum > target: return False
            if cursum == target: return dfs(nums, used, target, 0, k-1, 0)             

            for i in range(start, len(nums)):
                if used[i]: continue
                used[i] = True
                if dfs(nums, used, target, cursum + nums[i], k, i+1):
                    return True
                used[i] = False                
            return False
        
        return dfs(nums, used, target, 0, k, 0)
    # 1st trial with help from http://www.cnblogs.com/grandyang/p/7733098.html, TLE
    def canPartitionKSubsets3(self, nums, k):
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

nums, k = [4,5,3,2,1,3,5,2, 5, 5, 5, 5, 5, 5, 5, 5], 13
#nums, k = [4, 3, 2, 3, 5, 2, 1], 4
print(Solution().canPartitionKSubsets2(nums, k))