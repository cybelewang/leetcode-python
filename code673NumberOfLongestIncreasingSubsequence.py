"""
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

"""
# similar problems: 300 Longest Increasing Subsequence
class Solution:
    # my own solution with bug fixed
    # initially just use max length in dp, but forgot the count
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[1, 1] for _ in range(n)] # dp[i] contains the length and count of LIS ending with nums[i]

        max_len = 1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 > dp[i][0]: # update max length and count
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[j][0] + 1 == dp[i][0]:  # update count
                        dp[i][1] += dp[j][1]

            max_len = max(max_len, dp[i][0])

        print(dp)
        count = 0
        for len_, cnt in dp:
            if len_ == max_len:
                count += cnt

        return count
nums = [1, 3, 2, 4, 5, 6]
obj = Solution()
print(obj.findNumberOfLIS(nums))
