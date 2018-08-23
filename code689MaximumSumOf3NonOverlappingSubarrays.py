"""
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
"""
class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
    # my own O(N^2) solution, TLE
    # generate a list k_sum[i], value is the sum of k numbers starting from index i
    # get a list max_k_sum[i], value is the index j in k_sum, with k_sum[j] is the largest in range k_sum[i:]
    # then we iterate nums with i and j, and can find the third largest k_sum with the help of max_k_sum
    def maxSumOfThreeSubarrays2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        k_sum = [0]*(n-k+1)

        k_sum[0] = sum(nums[:k])    # sum of k numbers starting from index i
        for i in range(1, n-k+1):
            k_sum[i] = k_sum[i-1] - nums[i-1] + nums[i+k-1]

        max_k_sum_index = list(range(n-k+1))    # max_k_sum_index[i] is the index j, which has the max k sum for j in range [i:]
        for i in range(n-k-1, -1, -1):
            if k_sum[max_k_sum_index[i+1]] > k_sum[i]:
                max_k_sum_index[i] = max_k_sum_index[i+1]

        max_sum, res = 0, [0, k, 2*k]
        for i in range(n-3*k+1):
            for j in range(i+k, n-2*k+1):
                current = k_sum[i] + k_sum[j] + k_sum[max_k_sum_index[j+k]]
                if current > max_sum:
                    max_sum = current
                    res = [i, j, max_k_sum_index[j+k]]
                else:
                    res = min(res, [i, j, max_k_sum_index[j+k]])
        
        return res

nums = list(range(20000))
k = 2
print(Solution().maxSumOfThreeSubarrays(nums, k))
