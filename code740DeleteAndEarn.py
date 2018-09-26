"""
740 Delete and Earn

Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:
Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
Example 2:
Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation: 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
Note:

The length of nums is at most 20000.
Each element nums[i] is an integer in the range [1, 10000].
"""
from collections import Counter
class Solution:
    # my own solution using DP
    # to handle duplicated numbers, we convert nums to unique sorted numbers list, and use a counter map to record the repetition of the number
    # dp[i] is the points earned when using nums[i] as the last delete number
    # if nums[i-1] < nums[i] - 1, we can add dp[i-1]
    # if nums[i-1] == nums[i] - 1, we should skip dp[i-1] and use dp[i-2]
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        sort_nums = sorted(count.keys())
        n = len(sort_nums)

        res, dp = 0, [0]*n
        for i, num in enumerate(sort_nums):
            dp[i] = num*count[num]
            if i > 0 and sort_nums[i-1] < num - 1:
                dp[i] += dp[i-1]
            elif i > 1 and sort_nums[i-1] == num - 1:
                dp[i] += dp[i-2]
        
            res = max(res, dp[i])

        return res

test_nums = [[], [1,2,1], [3,4,2], [2, 2, 3, 3, 3, 4], [1, 3, 5, 7, 9]]
obj = Solution()
for nums in test_nums:
    print(obj.deleteAndEarn(nums))
