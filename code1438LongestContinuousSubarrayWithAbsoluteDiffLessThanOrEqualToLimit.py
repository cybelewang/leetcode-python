"""
1438 Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
"""
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # maintain a mono-decrease queue for max value of the window
        # and a mono-increase deque for min value of the window
        # use two pointers to get the max size window
        monoInc, monoDec = deque(), deque()
        i, n = 0, len(nums)
        res = 0
        for j in range(n):
            while monoDec and nums[monoDec[-1]] <= nums[j]:
                monoDec.pop()
            while monoInc and nums[monoInc[-1]] >= nums[j]:
                monoInc.pop()
            monoDec.append(j)
            monoInc.append(j)
            while monoDec and monoInc and nums[monoDec[0]] - nums[monoInc[0]] > limit:
                i += 1
                if i > monoDec[0]:
                    monoDec.popleft()
                if i > monoInc[0]:
                    monoInc.popleft()

            res = max(res, j-i+1)
        
        return res
