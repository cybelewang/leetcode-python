"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""
# if robbing day i, we cannot rob day i-1, but can rob day i-2, i-3, ... 0 
# Therefore if we use t[i] represents the max amount on day i, we have t[i] = max(t[i-1], t[i-2] + nums[i])
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 1:
            return 0
        elif n < 2:
            return nums[0]
        elif n < 3:
            return max(nums[0], nums[1])
        
        if nums[1] < nums[0]:
            nums[1] = nums[0]
        
        for i in range(2, n):
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])
        
        return nums[-1]

test_case = [0, 10, 3, 5, 15, 7, 0]
obj = Solution()
print(obj.rob(test_case))