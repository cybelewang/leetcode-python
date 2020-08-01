"""
689 Maximum Sum of 3 Non-Overlapping Subarrays

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
    # help from http://www.cnblogs.com/grandyang/p/8453386.html
    # left[i] is the smallest start index of size-k subarray with max sum in nums[:i+1]
    # right[i] is the smallest start index of size-k subarray with max sum in nums[i:]
    # good problem to practice index calculation
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n, sums = len(nums), [0]
        for num in nums: sums.append(sums[-1] + num)
        
        maxSum, left = 0, [0]*n
        for i in range(k-1, n):
            total = sums[i+1] - sums[i-k+1]
            if total > maxSum:
                maxSum = total
                left[i] = i-k+1
            else:
                left[i] = left[i-1]
        
        maxSum, right = 0, [n-k]*n
        for j in range(n-k, -1, -1):
            total = sums[j+k] - sums[j]
            if total >= maxSum: # bug fixed: we must use >= to ensure the index is smallest, not >
                maxSum = total
                right[j] = j
            else:
                right[j] = right[j+1]
        
        maxSum, res = 0, []
        for i in range(k, n-2*k+1):
            l, r = left[i-1], right[i+k]
            total = sums[l+k] - sums[l] + sums[i+k] - sums[i] + sums[r+k] - sums[r]
            if total > maxSum:
                maxSum = total
                res = [l, i, r]
        
        return res
        

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

    # 7/31/2020, brutal force solution
    # get 3 non-overlapping subarrays and use a getMax function to find their max sum
    # O(N^3), TLE
    def maxSumOfThreeSubarrays3(self, nums, k):
        def getMax(sums, s, e):
            maxSum, idx = 0, e-k
            for i in range(s, e-k+1):
                rangeSum = sums[i+k] - sums[i]
                if rangeSum > maxSum:
                    maxSum = rangeSum
                    idx = i
            return (maxSum, idx)
        
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        
        maxTotal = 0
        n = len(nums)
        res = []
        # we will split nums to 3 subarrays: [:i], [i:j], [j:]
        for i in range(k, n-2*k+1):
            for j in range(i+k, n-k+1):
                left, mid, right = getMax(sums, 0, i), getMax(sums, i, j), getMax(sums, j, n)
                total = left[0]+mid[0]+right[0]
                if total > maxTotal:
                    #print(total)
                    maxTotal = total
                    res = [left[1], mid[1], right[1]]
                    #print(res)
        
        return res

#nums = list(range(20000))
#nums, k = [7,13,20,19,19,2,10,1,1,19], 3 # expect [1,4,7]
nums, k = [1,2,1,2,1,2,1,2,1],2 # expect [0,2,4]
print(Solution().maxSumOfThreeSubarrays4(nums, k))
